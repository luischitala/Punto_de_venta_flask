from flask import Flask, render_template, url_for, redirect, request
import json
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/insert/default")
def instert_default():
    new_post = Posts(title="Default Title")
    db.session.add(new_post)
    db.session.commit()

    return "Te default post was created."

@app.route("/select/default")
def select_default():
    post = Posts.query.filter_by(id=1).first()

    print(post.title)
    return "Query Done."

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
