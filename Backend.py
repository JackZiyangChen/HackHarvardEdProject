from flask import Flask, request, redirect
import json

# Defining application
app = Flask(__name__)


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
    id = []
    count = []
    try:
        id = request.args.getlist('id')
        count = request.args.getlist('count')
        print(id, count)
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)

    return json.dumps({
        'status': status,
        'description': description,
        'id': id,
        'count': count
    })


# Api for recommending colleges by name
@app.route('/recommend/college_name')
def recommend_college_by_name():
    colleges = []
    try:
        colleges = request.args.getlist('college')
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)


    return json.dumps({
        'status': status,
        'description': description,
        'colleges': colleges
    })


# Api for recommending colleges by user id
@app.route('/recommend/user')
def recommend_user():
    # Get user's location/information after OAuth

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


    return json.dumps({
        'status': status,
        'description': description,
        'Country': userCountry,
        'Zip Code': userZip
    })


# Api for recommending colleges by id
@app.route('/predict')
def predict_for_user():
    # Get user's location/information after OAuth

    try:
        userId = request.args.get('user')
        collegeName = request.args.get('college')
        status = 200
        description = "Data retrieved successfully"

    except Exception as e:
        status = 404
        description = str(e)
        userId = ""
        collegeName = ""

    return json.dumps({
        'status': status,
        'description': description,
        'User ID': userId,
        'College Name': collegeName
    })


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
    app.run()