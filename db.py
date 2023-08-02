########## Imports: ##########

import sqlite3



########## DB Functions: ##########

def setup(filename="tasks.sqlite"):
    '''Creating the DB if not exists.'''
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, category TEXT, description TEXT, date TEXT)")
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
    tasks = query_db(sql)["rows"]
    keys = query_db(sql)["keys"]
    
    tasks_dict = []
    for task in tasks:
        values = list(task)
        tempd = dict(zip(keys, values))
        tasks_dict.append(tempd)
    return tasks_dict



########## Temp Functions: ##########

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
    





# Temp:

# setup()


