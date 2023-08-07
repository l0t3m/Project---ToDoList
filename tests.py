from faker import Faker
import random
import db
import sqlite3

fake = Faker()



########## Test Functions: ##########

def create_fake_tasks(num, filename):
    for i in range(num):
        category = random_category(filename)
        description = "fake_description"
        date = fake.future_date()
        
        db.query_db(sql=f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')", filename=filename)

def random_category(filename):
    category = db.query_db(sql="SELECT * FROM categories", filename=filename)
    return random.choice(category["rows"])[1]

def simple_query_db(sql, filename):
    '''Executes the sql given and returns the results.'''
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
