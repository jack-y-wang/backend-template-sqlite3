import json
import os
import datetime

from db import db
import dao
from utils import *

from flask import Flask, request

app = Flask(__name__)
db_filename = "backend-template.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def welcome():
    return "Welcome to Backend Template! :)"

# USER ROUTES ----------------------------------------------
@app.route("/users/", methods=["GET"])
def get_users():
    return success_response([user.serialize() for user in dao.get_users()])

@app.route("/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    name = body.get("name")
    email = body.get("email")
    username = body.get("username")

    optional_user, err = dao.create_user(name, email, username)
    if not optional_user:
        return failure_response(err)
    return success_response(optional_user.serialize(), 201)

@app.route("/users/<int:user_id>/", methods=["GET"])
def get_user(user_id):
    user, err = dao.get_user_by_id(user_id)
    if not user:
        return failure_response(err)
    return success_response(user.serialize())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)