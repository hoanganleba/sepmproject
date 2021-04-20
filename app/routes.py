from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/team')
def team():
    return render_template("team.html")
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")