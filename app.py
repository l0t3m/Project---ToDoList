from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
import functions
import db

db.setup("tasks.sqlite")

### Tasks Routes: ###

@app.route('/')
def home():
    return render_template('home.html', tasks = functions.get_tasks_sorted(), tabs = functions.get_tabs())

@app.route('/delete-task')
def delete():
    functions.delete_task(request.args['task_id'])
    return redirect(url_for("home"))

@app.route('/add-task')
def add():
    return render_template('add.html', categories = functions.get_categories(), tabs = functions.get_tabs())

@app.route('/add-task-db')
def add_to_db():
    category = request.args["categories"]
    description = request.args["description"]
    date = request.args["date"]

    if len(description) == 0 or len(date) == 0:
        return redirect(url_for("add"))

    functions.add_task(category, description, date)
    return redirect(url_for("home"))

@app.route('/search-task')
def search_task():
    query = request.args["search-value"]
    return render_template('home.html', tasks = functions.search_task(query), tabs = functions.get_tabs())

@app.route('/update-task')
def update_task():
    task_id = request.args["task_id"]

    return render_template('update-task.html', task = functions.get_task(task_id), tabs = functions.get_tabs(), categories = functions.get_categories())

@app.route('/update-task-to-db')
def update_task_to_db():
    task_id = request.args["task_id"]
    task_category = request.args["categories"]
    task_description = request.args["description"]
    task_date = request.args["date"]

    functions.update_task(task_id, task_category, task_description, task_date)
    return redirect(url_for("home"))


### Categories Routes: ###

@app.route('/categories')
def all_categories():
    return render_template('categories.html', categories = functions.get_categories(), tabs = functions.get_tabs())

@app.route('/delete-category')
def delete_category():
    functions.delete_existing_category(request.args["category_id"])
    return redirect(url_for("all_categories"))

@app.route('/add-category')
def add_category():
    return render_template('categories-add.html', tabs = functions.get_tabs())

@app.route('/add-category-db')
def add_category_to_db():
    category = request.args["category-name"]

    if len(category) == 0:
        return redirect(url_for("add_category"))

    functions.add_new_category(category)
    return redirect(url_for("all_categories"))

@app.route('/search-category')
def search_category():
    category = request.args["search-value"]
    return render_template('categories.html', categories = functions.search_category(category), tabs = functions.get_tabs())

@app.route('/update-category')
def update_category():
    category_id = request.args["category_id"]
    return render_template('update-category.html', category = functions.get_category(category_id), tabs = functions.get_tabs())

@app.route('/update-category-to-db')
def update_category_to_db():
    category_id = request.args["category_id"]
    category_name = request.args["category_name"]

    functions.update_category(category_id, category_name)
    return redirect(url_for("all_categories"))