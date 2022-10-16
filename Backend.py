from flask import Flask, request, redirect, jsonify
import json
from ML.models.CollabFilter import CollabFilter, CollegeCollegeRecommender, UserUserRecommender
from util.RestResponse import RestResponse
from util.data import *

# Defining application
app = Flask(__name__)


# App configuration
app.config['JSON_SORT_KEYS'] = False

# initialize college model
ccr = CollegeCollegeRecommender()
uur = UserUserRecommender() 

def init_models():
    
    # populate dataframe with data from database
    raw = json.load(open('database/College_Data_Dict.json'))
    arr = []

    for item in raw:
        arr.append(item)
    ccr.populate_df(arr)

    ccr.clean_data()
    # print(ccr.df_clean.head(5))
    uur.clean_data()


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
# not supported
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
    init_models()
    ccr.run()
    res = RestResponse(200, request, {})
    res.populate_request(request)

    colleges = []
    data = {}
    try:
        if request.method == 'GET':
            colleges = request.args.getlist('college')
        elif request.method == 'POST':
            colleges = request.form.getlist('college')
        print(colleges)
        for c in colleges:
            i = get_index_by_attribute(ccr.df, 'name', c)
            print(i)
            data = dataframe_to_dict(ccr.get_similar(i))

    except Exception as e:
        print(e)
        res.set_status(500)
        res.custom_message = str(e)

    res.populate_data(data)

    return jsonify(res.generate_response()), res.status


# Api for recommending colleges by user id
@app.route('/recommend/user')
def recommend_user():
    # Get user's location/information after OAuth
    res = RestResponse(200, request, {})
    res.populate_request(request)
    data = {}
    user_id = 0
    if request.method == 'GET':
        user_id = request.args.get('user')
    elif request.method == 'POST':
        user_id = request.form.get('user')

    
    try:
        status = 200

        #TODO: update data with user's information

        uur.clean_data().run()

        i = get_index_by_attribute(ccr.result, 'User-id', user_id)
        userlist = dataframe_to_dict(ccr.get_similar(i, n=5))
        

        # query user to find their colleges

        # aggregate colleges

        # feedback top 5 count



        

    except Exception as e:
        status = 504
        res.custom_message = f'Internal Server Error: {str(e)}'


    res.set_status(status).populate_data(data)
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


# Api for retrieving user data from DB
@app.route('/db/get')
def get_data_from_db():
    # Get user's location/information after OAuth

    try:
        userId = request.args.get('user')
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)
        userId = ""

    return json.dumps({
        'status': status,
        'description': description,
        'User ID': userId,
    })


# Api for posting user data to DB
@app.route('/db/get', methods=['POST'])
def post_data_to_db():
    # Get user's location/information after OAuth

    try:
        userId = request.args.get('user')
        username = request.args.get('username')
        email = request.args.get('email')
        fname = request.args.get('fname')
        lname = request.args.get('lname')
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)
        userId = ""
        username = ""
        email = ""
        fname = ""
        lname = ""

    return json.dumps({
        'status': status,
        'description': description,
        'User ID': userId,
        'Username': username,
        'Email': email,
        'First Name': fname,
        'Last Name': lname
    })


# Running application
if __name__ == '__main__':
    app.run(debug=True) # will be disabled on production