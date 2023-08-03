import db

def get_tasks_sorted():
    '''Returns all the tasks sorted as multiple dicts in a list from the db.'''
    tasks = sorted(db.get_dicts(), key=lambda i:i["date"])
    return tasks

def get_categories():
    '''Returns all the categories as multiple dicts in a list from the db.'''
    categories = db.get_dicts("SELECT * FROM categories")
    return categories

def get_tabs():
    '''Returns all the tabs and url for them as multiple dicts in a list.'''
    tabs = {
        "All Tasks":"/",
        "Add a Task":"/add-task",
        "All Categories":"/categories",
        "Add a Category":"/add-category",
    }
    return list(tabs)


########## Actions: ##########

def delete_task(task_id):
    db.query_db(sql=f"DELETE FROM tasks WHERE task_id='{task_id}';")

def add_task(category, description, date):
    db.query_db(sql=f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')")




