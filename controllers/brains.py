from flask_app import app
from flask import render_template, redirect, request

@app.route("/")
def brain():
    return render_template("index.html")

@app.route("/buyModel")
def buymodel():
    return render_template("buyModel.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/aboutus")
def abus():
    return render_template("aboutus.html")

@app.route("/createaccount")
def createaccount():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")