from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
from functions import *

#########################################################################################

@app.route('/')
def home():
    return render_template('home.html', tasks = get_tasks_sorted(), tabs = get_tabs())


@app.route('/delete')
def delete():
    delete_task(request.args['task_id'])
    return redirect(url_for("home"))


@app.route('/add-task')
def add():
    return render_template('add.html', categories = get_categories(), tabs = get_tabs())


@app.route('/add-task-db')
def add_to_db():
    category = request.args["categories"]
    description = request.args["description"]
    date = request.args["date"]

    add_task(category, description, date)
    return redirect(url_for("home"))


#########################################################################################


@app.route('/categories')
def all_categories():
    return render_template('categories.html', categories = get_categories(), tabs = get_tabs())


@app.route('/delete-category')
def delete_category():
    delete_existing_category(request.args["category_id"])
    return redirect(url_for("all_categories"))


@app.route('/add-category')
def add_category():
    return render_template('categories-add.html', tabs = get_tabs())


@app.route('/add-category-db')
def add_category_to_db():
    category = request.args["category-name"]

    add_new_category(category)
    return redirect(url_for("all_categories"))


#########################################################################################