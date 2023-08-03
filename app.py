from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
from functions import *

@app.route('/')
def home():
    return render_template('home.html', tasks = get_tasks_sorted())

@app.route('/delete')
def delete():
    delete_task(request.args['task_id'])
    return redirect(url_for("home"))

@app.route('/add-task')
def add():
    return render_template('add.html', categories = get_categories())

@app.route('/add-task-db')
def add_to_db():
    category = request.args["categories"]
    description = request.args["description"]
    date = request.args["date"]

    add_task(category, description, date)
    return redirect(url_for("home"))

@app.route('/categories')
def all_categories():
    return render_template("categories.html", categories = get_categories())



