import json
from flask import Flask, Request


class RestResponse:

    HTTPMESSAGE = {
        "202": "Accepted",
        "502": "Bad Gateway",
        "400": "Bad Request",
        "409": "Conflict",
        "100": "Continue",
        "201": "Created",
        "417": "Expectation Failed",
        "424": "Failed Dependency",
        "403": "Forbidden",
        "504": "Gateway Timeout",
        "410": "Gone",
        "505": "HTTP Version Not Supported",
        "418": "I'm a teapot",
        "419": "Insufficient Space on Resource",
        "507": "Insufficient Storage",
        "500": "Internal Server Error",
        "411": "Length Required",
        "423": "Locked",
        "420": "Method Failure",
        "405": "Method Not Allowed",
        "301": "Moved Permanently",
        "302": "Moved Temporarily",
        "207": "Multi-Status",
        "300": "Multiple Choices",
        "511": "Network Authentication Required",
        "204": "No Content",
        "203": "Non Authoritative Information",
        "406": "Not Acceptable",
        "404": "Not Found",
        "501": "Not Implemented",
        "304": "Not Modified",
        "200": "OK",
        "206": "Partial Content",
        "402": "Payment Required",
        "308": "Permanent Redirect",
        "412": "Precondition Failed",
        "428": "Precondition Required",
        "102": "Processing",
        "407": "Proxy Authentication Required",
        "431": "Request Header Fields Too Large",
        "408": "Request Timeout",
        "413": "Request Entity Too Large",
        "414": "Request-URI Too Long",
        "416": "Requested Range Not Satisfiable",
        "205": "Reset Content",
        "303": "See Other",
        "503": "Service Unavailable",
        "101": "Switching Protocols",
        "307": "Temporary Redirect",
        "429": "Too Many Requests",
        "401": "Unauthorized",
        "451": "Unavailable For Legal Reasons",
        "422": "Unprocessable Entity",
        "415": "Unsupported Media Type",
        "305": "Use Proxy",
        "421": "Misdirected Request"
    }

    def __init__(self, status, request, data):
        self.status = status
        self.request = request
        self.data = data
        self.paginate = False
        self.custom_message = ''

    def populate_request(self, request: Request):
        
        self.request = {}
        self.request['api'] = request.host
        self.request['path'] = request.path
        self.request['method'] = request.method
        self.request['endpoint'] = request.endpoint
        self.request['args'] = request.args
        self.request['content_type'] = request.content_type
        self.request['cookies'] = request.cookies
        self.request['content_encoding'] = request.content_encoding
        return self
        

    def populate_data(self, data):
        self.data = data
        return self

    def set_status(self, status):
        self.status = status
        return self

    def generate_paginate(self, page, per_page, total):
        return self
    
    def make_json(self):
        return json.dumps(self.generate_response())
    
    def generate_response(self):
        res = {
            'success': self.status//100==2, # 2xx is success
            'status': self.status,
            'message': self.custom_message or self.HTTPMESSAGE[str(self.status)],
            'request': self.request,
            'data': self.data,
            'paginate': self.paginate,
            'links':{
                'current': self.request['api'] + self.request['path'] # TODO: customly populate this
            }
        }

        return res