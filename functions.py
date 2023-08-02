import db

def get_tasks():
    '''Returns all the tasks as a dicts on the list from the db.'''
    tasks = db.get_dicts()
    # orders=sorted(get_dicts(), key=lambda i: i["time"][:2])
    return tasks

def delete_task(id):
    db.query_db(sql=f"DELETE FROM tasks WHERE id='{id}';")




