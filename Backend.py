from flask import Flask, request, redirect, jsonify
import json
from util.RestResponse import RestResponse

# Defining application
app = Flask(__name__)


# App configuration
app.config['JSON_SORT_KEYS'] = False


# Api for landing page
@app.route('/')
def landing_page():
    return redirect("/homepage")


# Api for homepage
@app.route('/homepage')
def homepage():
    return """
        <h1>List of apis</h1>
        <h3>/recommend/college_id?id={id}&count={#}</h3>
        <h3>/recommend/college_name?college={college1}&college={college2}&college={college3}...</h3>
        <h3>/recommend/user</h3>
        <h3>/predict?user={userId}&college={collegeName}</h3>

        <h1>Apis for communication to DB</h1>
        <h3>/db/get/user={username}</h3>
        <h3>/db/post</h3>
        """


# Api for recommending colleges by id
@app.route('/recommend/college_id')
def recommend_college_by_id():
    res = RestResponse(200, request, {}) # initialize rest response
    res.populate_request(request) # populate request header
    data = {}

    id = []
    count = []
    try:
        id = request.args.getlist('id')
        count = request.args.getlist('count')
        print(id, count)
        data = {}

    except Exception as e:
        res.set_status(504)

    res.populate_data(data)
    return jsonify(res.generate_response()), res.status # generate a dictionary -> json


# Api for recommending colleges by name
@app.route('/recommend/college_name')
def recommend_college_by_name():
    res = RestResponse(200, request, {})
    res.populate_request(request)

    colleges = []
    data = {}
    try:
        colleges = request.args.getlist('college')
        status = 200
        description = "Data retrieved successfully"
        data = {
            'status': status,
            'description': description,
            'colleges': colleges
        }
        

    except Exception as e:
        res.set_status(504).populate_data({})

    res.populate_data(data)

    return jsonify(res.generate_response()), res.status


# Api for recommending colleges by user id
@app.route('/recommend/user')
def recommend_user():
    # Get user's location/information after OAuth
    res = RestResponse(200, request, {})
    res.populate_request(request)
    data = {}

    try:
        userCountry = "User's country"
        userZip = "User's Zip Code"
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)
        userCountry = ""
        userZip = ""

    res.populate_data(data)
    return jsonify(res.generate_response()), res.status


# Api for recommending colleges by id
@app.route('/predict')
def predict_for_user():
    # Get user's location/information after OAuth

    res = RestResponse(200, request, {})
    res.populate_request(request)
    data = {}

    try:
        userId = request.args.get('user')
        collegeName = request.args.get('college')
        status = 200
        data = {
            'status': status,
            'User ID': userId,
            'College Name': collegeName
        }

    except Exception as e:
        status = 404
        description = str(e)
        userId = ""
        collegeName = ""

    res.populate_data(data)
    res.set_status(status)



    return jsonify(res.generate_response()), res.status


# Running application
if __name__ == '__main__':
    app.run(debug=True) # will be disabled on production