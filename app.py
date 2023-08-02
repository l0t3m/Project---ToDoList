from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
from functions import *

@app.route('/')
def home():
    return render_template('home.html', tasks = get_tasks())

@app.route('/add')
def add():
    return render_template('add.html', categories = get_categories())

@app.route('/delete')
def delete():
    delete_task(request.args['task_id'])
    return redirect(url_for("home"))


