import db

def get_tasks():
    
    tasks = db.get_dicts()
    # orders=sorted(get_dicts(), key=lambda i: i["time"][:2])
    return tasks

tasks = get_tasks()
print(tasks)




