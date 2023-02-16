from flask import Flask, render_template, request, session, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from flask_mail import Message
import json
import math


app = Flask(__name__)


@app.route("/saikumar1277.github.io/newpro")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/certification")
def certification():
    return render_template("certification.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
