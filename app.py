from http import client
from re import L
from flask import g, redirect, request
from wsgiref.util import request_uri
from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/homework3"
mongo = PyMongo(app)

@app.route('/', methods=["GET", "POST"])
def index():
    postsFromDB = list(mongo.db.posts.find())

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = mongo.db.users.find_one({
            "username" : username
        })
        if password == (user['password']):
            return render_template("story.html", posts = postsFromDB, username = user['username'])
        else:
            return 'Access denied'

    else:
        return render_template("index.html")

@app.route('/story', methods=["GET", "POST"])
def story():
    postsFromDB = list(mongo.db.posts.find())
    if request.method == "POST":
        article = {
            "title": request.form.get("title"),
            "text": request.form.get("text")
        }
        mongo.db.posts.insert_one(article)
    return render_template("story.html", posts = postsFromDB)

app.run(host="localhost", port=5000, debug=True)