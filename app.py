from http import client
from re import L
from flask import g, redirect, request
from wsgiref.util import request_uri
from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/homework2"
mongo = PyMongo(app)

@app.route('/')
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = mongo.db.users.find_one({
            "username" : username
        })
        if password == (user['password']):
            return render_template("profile.html")
        else:
            return 'Access denied'

    else:
        return render_template("index.html")

app.run(host="localhost", port=5000, debug=True)