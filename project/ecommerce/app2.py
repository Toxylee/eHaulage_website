from flask import Flask, jsonify, request, session
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt
import jwt
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS, cross_origin

app2 = Flask(__name__)
jwt = JWTManager(app2)
CORS(app2)

app2.config["MONGO_URI"] = "mongodb+srv://toxylee20021:pFQEit2RjN6yWNmz@cluster0.qaw64wf.mongodb.net/CartIT?retryWrites=true&w=majority"
mongo = PyMongo(app2)

app2.secret_key = 'super secret key'
app2.config["JWT_SECRET_KEY"] = "this-is-secret-key"

@app2.route("/")
def hello_world():
    return "Hello World"

@app2.route("/userSignUp", methods=['POST', 'GET'])
def userSignUp():
    if request.method == 'POST':
        allUsers = mongo.db.users
        user = allUsers.find_one({'email': request.json['email']})
        username = allUsers.find_one({'username': request.json['username']})
        phone = allUsers.find_one({'phone': request.json['phone']})

        if user:
            return jsonify(message='Email already exists'), 401
        if username:
            return jsonify(message='Username already exists'), 401
        if phone:
            return jsonify(message='Phone Number already exists'), 401

        if request.json['password'] != request.json['cpassword']:
            return jsonify(message='Password Not Matching!'), 401

        hashpw = bcrypt.hashpw(
            request.json['password'].encode('utf-8'), bcrypt.gensalt())

        hashCpw = bcrypt.hashpw(
            request.json['cpassword'].encode('utf-8'), bcrypt.gensalt())

        access_token = create_access_token(identity=request.json['email'])

        allUsers.insert({
            'email': request.json['email'],
            'password': hashpw,
            'cpassword': hashCpw,
            "username": request.json['username'],
            "phone": request.json['phone'],
            'tokens': [
                {
                    'token': str(access_token)
                }
            ]
        })

        session['email'] = request.json['email']
        return jsonify(token=str(access_token)), 201


@app2.route("/userLogin", methods=['POST'])
def userLogin():
    allUsers = mongo.db.users
    user = allUsers.find_one({'email': request.json['email']})

    if user:
        if bcrypt.hashpw(request.json['password'].encode('utf-8'), user['password']) == user['password']:
            # session['email'] = request.json['email']
            access_token = create_access_token(identity=request.json['email'])
            user['tokens'].append({'token': str(access_token)})
            allUsers.save(user)
            return jsonify(token=str(access_token)), 201
    return jsonify(message='Invalid Username/Password'), 401


if __name__ == '__main__':
    app2.run(debug=true)
