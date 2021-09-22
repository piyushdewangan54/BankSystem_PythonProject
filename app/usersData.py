from flask import Flask, jsonify, request, make_response
from config import client
from app import app
import json

db = client.restfulapi

collection = db['BankAPI']

@app.route("/hello")
def index():
    return '<h1> Hello World </h1>'

# Below function is used to create user account inside Bank

@app.route("/createUser", methods = ["POST"])
def create_user():
    records = request.get_json()
    if records:
        if "contact" in records:
            collection.insert_one(records)
            return make_response(jsonify({"MSG":"Record inserted..."}),200)
        else:
            return make_response(jsonify({"ERROR": "Please provide contact number..."}), 403)
    else:
        return make_response(jsonify({"ERROR":"Please provide whole information..."}),404)

# Below function is used to retrieve information of the Bank User

@app.route("/getUser/<id>", methods= ["GET"])
def get_user(id):
    user_data = collection.find_one({"_id":int(id)})
    if user_data:
        return make_response(jsonify(user_data), 200)
    else:
        return make_response(jsonify({"error":"Record not foun0d..."}),406)

# Below function is used to Update the records of the user

@app.route("/updateUser/<id>", methods = ["PUT"])
def update_user(id):
    data = request.get_json()
    user_data = collection.find_one({"_id":int(id)})
    if user_data:
        collection.update_one({"_id":int(id)},{"$set":data})
        return make_response(jsonify({"MSG": "Information Updated Successfully..."}), 200)
    else:
        return make_response(jsonify({"ERROR": "NO Record found..."}), 400)

# Below function is used to delete the desired Bank user

@app.route("/deleteUser/<id>", methods = ["DELETE"])
def delete_user(id):
    user_data = collection.find_one({"_id": int(id)})
    if user_data:
        collection.delete_one({"_id":int(id)})
        return make_response(jsonify({"MSG": "User Deleted Successfully..."}), 200)
    else:
        return make_response(jsonify({"ERROR": "NO Record found..."}), 400)