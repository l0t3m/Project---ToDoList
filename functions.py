import db

def get_tasks_sorted():
    '''Returns all the tasks sorted as multiple dicts in a list.'''
    return sorted(db.get_dicts(), key=lambda i:i["date"])

def get_categories():
    '''Returns all the categories as multiple dicts in a list.'''
    return db.get_dicts("SELECT * FROM categories", "tasks.sqlite")

def get_tabs():
    '''Returns all the tabs and url for them as multiple dicts in a list.'''
    return list(db.get_dicts("SELECT * FROM tabs", "tasks.sqlite"))

### Tasks: ###

def get_task(task_id):
    '''Gets the task id and looks for it through the db, returns list containing dicts with results.'''
    return list(db.get_dicts(f"SELECT * FROM tasks WHERE task_id = '{task_id}'", "tasks.sqlite"))

def delete_task(task_id):
    '''Gets the task id and removes it through the db.'''
    db.query_db(sql=f"DELETE FROM tasks WHERE task_id='{task_id}';")

def add_task(category, description, date):
    '''Gets the category, description, date and adds it to the db.'''
    db.query_db(sql=f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')")

def search_task(query):
    '''Gets a query and looks for anything like that in the db, returns a list containing dicts with results.'''
    return db.get_dicts(f"SELECT * FROM tasks WHERE category LIKE '%{query}%' or description like '%{query}%' or date like '%{query}%';", "tasks.sqlite")

def update_task(task_id, new_category, new_description, new_date):
    '''Gets the task id, removes it and adding the new info to the db.'''
    delete_task(task_id)
    add_task(new_category, new_description, new_date)

### Categories: ###

def get_category(category_id):
    '''Gets the category id and looks for it through the db, returns list containing dicts with results.'''
    return list(db.get_dicts(f"SELECT * FROM categories WHERE category_id = '{category_id}'", "tasks.sqlite"))

def delete_existing_category(category_id):
    '''Gets the category id and removes it through the db.'''
    db.query_db(sql=f"DELETE FROM categories WHERE category_id='{category_id}'")

def add_new_category(category_name):
    '''Gets the category name and inserts it to the db.'''
    db.query_db(sql=f"INSERT INTO categories(category_name) VALUES ('{category_name}')")

def search_category(category_name):
    '''Gets a category name and looks for anything like that in the db, returns a list containing dicts with results.'''
    return db.get_dicts(f"SELECT * FROM categories WHERE category_name LIKE '%{category_name}%'", "tasks.sqlite")

def update_category(category_id, category_name):
    '''Gets the category id, removes it and adding the new info to the db.'''
    delete_existing_category(category_id)
    add_new_category(category_name)

