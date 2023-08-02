########## Imports: ##########

from faker import Faker
import random
import datetime
import db



########## Global Variables: ##########
fake = Faker()
fake_categories = ["Home", "Car", "Dog"]



########## Test Functions: ##########

def create_fake_tasks(num):
    for i in range(num):
        category = random.choice(fake_categories)
        description = "fake_description"
        date = fake.future_date()
    
        sql = f"INSERT INTO tasks (category, description, date) VALUES ('{category}', '{description}', '{date}')"
        db.query_db(sql=sql)


# create_fake_tasks(20)





