########## Imports: ##########

from faker import Faker
import random
import datetime
import db



########## Global Variables: ##########

fake = Faker()



########## Test Functions: ##########

def create_fake_tasks(num):
    for i in range(num):
        category = random_category()
        description = "fake_description"
        date = fake.future_date()
        
        db.query_db(sql=f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')")



########## Additional Functions: ##########

def random_category():
    category = db.query_db(sql="SELECT * FROM categories", filename="tasks.sqlite")
    return random.choice(category["rows"])[1]



########## temp: ##########
# db.setup()
# create_fake_tasks(10)
