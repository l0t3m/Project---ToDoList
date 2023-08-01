from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')





