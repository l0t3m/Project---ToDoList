import db

def get_tasks():
    '''Returns all the tasks as multiple dicts in a list from the db.'''
    tasks = db.get_dicts()
    # orders=sorted(get_dicts(), key=lambda i: i["time"][:2])
    return tasks

def get_categories():
    '''Returns all the categories as multiple dicts in a list from the db.'''
    categories = db.get_dicts("SELECT * FROM categories")
    return categories

def delete_task(task_id):
    db.query_db(sql=f"DELETE FROM tasks WHERE task_id='{task_id}';")

def add_task(category, description, date):
    db.query_db(sql=f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')")




