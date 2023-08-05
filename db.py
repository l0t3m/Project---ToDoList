########## Imports: ##########

import sqlite3
import os



########## DB Functions: ##########

def setup(filename="tasks.sqlite"):
    '''Creating the DB if not exists.'''
    if os.path.exists('tasks.sqlite') == False:
        with sqlite3.connect(filename) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY, category TEXT, description TEXT, date TEXT)")
            cur.execute("CREATE TABLE IF NOT EXISTS categories(category_id INTEGER PRIMARY KEY, category_name TEXT)")
            cur.execute("CREATE TABLE IF NOT EXISTS tabs(tab_id INTEGER PRIMARY KEY, tab_name TEXT, tab_url TEXT)")
            conn.commit()

            setup_basic_info()

def setup_basic_info(filename="tasks.sqlite"):
    '''Creating basic data for the db.'''
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO categories (category_name) VALUES ('Personal Care'),('Health'),('Work'),('Chores');")
        cur.execute("INSERT INTO tabs (tab_name, tab_url) VALUES ('All Tasks', '/'),('Add a Task','/add-task'),('AllCategories','/categories'),('Add a Category','/add-category');")
        conn.commit()

def query_db(sql="SELECT * FROM tasks", filename="tasks.sqlite"):
    '''Returns a dict containing all the rows and keys of the sql.'''
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        row_names=[]
        try:
            for row in cur.description:
                row_names.append(row[0])
        except:
            row_names.append(get_keys())
        return {"rows":cur.fetchall(), "keys":row_names}

def get_dicts(sql="SELECT * FROM tasks"):
    '''Gets a sql and returns a dict containing the title(key) and row(value).'''
    tasks = query_db(sql)["rows"]
    keys = query_db(sql)["keys"]
    
    tasks_dict = []
    for task in tasks:
        values = list(task)
        tempd = dict(zip(keys, values))
        tasks_dict.append(tempd)
    return tasks_dict

def get_keys(sql="SELECT * FROM tasks", filename="tasks.sqlite"):
    '''Returns keys of the DB given.'''
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        row_names=[]
        for row in cur.description:
            row_names.append(row[0])
        return row_names
