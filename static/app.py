from flask import Flask, render_template, url_for, redirect, request
import json

app = Flask(__name__)

@app.route("/")

def hola_mundo():
    return "Hola mundo"


if __name__ == "__main__":
    app.run(debug = True)
