### Imports: ###
import unittest, os
import db, tests



### Unittests: ###

class DataBaseMethods(unittest.TestCase):
    def setUp(self):
        '''Creates the test file.'''
        self.test_file = "tasks-tests.sqlite"

        if os.path.exists(self.test_file) == False:
            db.setup(self.test_file)

    def tearDown(self):
        '''Deletes the DB.'''
        os.remove(self.test_file)


    ### setup: ###
    def test_setup(self):
        '''Tests if the test file exists.'''
        self.assertTrue(os.path.exists(self.test_file))
    
    def test_tasks_data(self):
        '''Tests if the table and info was created successfully.'''
        tasks = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        expected_result = []

        self.assertTrue(len(tasks) == 0)
        self.assertIsInstance(tasks, list)
        self.assertEqual(tasks, expected_result)
    
    def test_categories_data(self):
        '''Tests if the table and info was created successfully.'''
        categories = tests.simple_query_db(sql="SELECT * FROM categories", filename=self.test_file)
        expected_result = [(1, 'Personal Care'), (2, 'Health'), (3, 'Work'), (4, 'Chores')]

        self.assertTrue(len(categories) == 4)
        self.assertIsInstance(categories, list)
        self.assertEqual(categories, expected_result)

    def test_tabs_data(self):
        '''Tests if the table and info was created successfully.'''
        tabs = tests.simple_query_db(sql="SELECT * FROM tabs", filename=self.test_file)
        expected_result = [(1, 'All Tasks', '/'), (2, 'Add a Task', '/add-task'), (3, 'All Categories', '/categories'), (4, 'Add a Category', '/add-category')]

        self.assertTrue(len(tabs) == 4)
        self.assertIsInstance(tabs, list)
        self.assertEqual(tabs, expected_result)


    ### query_db: ###
    def test_query_db(self):
        '''Tests if query_db returns the data as expected'''
        result = db.query_db(sql="SELECT * FROM tabs", filename=self.test_file)
        expected_result = {'rows': [(1, 'All Tasks', '/'), (2, 'Add a Task', '/add-task'), (3, 'All Categories', '/categories'), (4, 'Add a Category', '/add-category')], 'keys': ['tab_id', 'tab_name', 'tab_url']}

        self.assertTrue(len(result) == 2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)

    def test_query_db_empty_table(self):
        '''Tests if query_db returns the data as expected but on an empty table.'''
        result = db.query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        expected_result = {'rows': [], 'keys': ['task_id', 'category', 'description', 'date']}

        self.assertTrue(len(result) == 2)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)


    ### get_dicts: ###
    def test_get_dicts(self):
        '''Tests if get_dicts returns the expected result.'''
        result = list(db.get_dicts(sql="SELECT * FROM tabs", filename=self.test_file))
        expected_result = [{'tab_id': 1, 'tab_name': 'All Tasks', 'tab_url': '/'}, {'tab_id': 2, 'tab_name': 'Add a Task', 'tab_url': '/add-task'}, {'tab_id': 3, 'tab_name': 'All Categories', 'tab_url': '/categories'}, {'tab_id': 4, 'tab_name': 'Add a Category', 'tab_url': '/add-category'}]

        self.assertTrue(len(result) == 4)
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_result)
    
    def test_get_dicts_empty_db(self):
        '''Tests if get_dicts returns the expected result, on an empty table.'''
        result = list(db.get_dicts(sql="SELECT * FROM tasks", filename=self.test_file))
        expected_result = ([])

        self.assertTrue(len(result) == 0)
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_result)


    ### get_keys: ###
    def test_get_keys(self):
        '''Tests if get_keys returns the expected result.'''
        result = db.get_keys(sql="SELECT * FROM tasks", filename=self.test_file)
        expected_result = ['task_id', 'category', 'description', 'date']

        self.assertTrue(len(result) == 4)
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_result)



class TestsMethods(unittest.TestCase):
    def setUp(self):
        '''Creates the test file.'''
        self.test_file = "tasks-tests.sqlite"

        if os.path.exists(self.test_file) == False:
            db.setup(self.test_file)

    def tearDown(self):
        '''Deletes the DB.'''
        os.remove(self.test_file)


    ### create_fake_tasks: ###
    def test_create_fake_tasks(self):
        '''Tests if create_fake_tasks actually makes the amount of tasks and inserting it to the DB.'''
        result = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        self.assertEqual(len(result), 0)

        tests.create_fake_tasks(10, self.test_file)
        result = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        self.assertEqual(len(result), 10)
    
    def test_create_fake_tasks_different_amounts(self):
        '''Tests if create_fake_tasks responding well with different amounts.'''
        result = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        self.assertEqual(len(result), 0)

        tests.create_fake_tasks(0, self.test_file)
        result = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        self.assertEqual(len(result), 0)

        tests.create_fake_tasks(-1, self.test_file)
        result = tests.simple_query_db(sql="SELECT * FROM tasks", filename=self.test_file)
        self.assertEqual(len(result), 0)


    ### random_category: ###
    def test_random_category(self):
        '''Tests if random_category is working properly.'''
        random_result = tests.random_category(filename=self.test_file)
        data = db.query_db(sql="SELECT * FROM categories", filename=self.test_file)

        for row in data["rows"]:
            if row[1] == random_result:
                self.assertIn(random_result, row[1])


    ### simple_query_db: ###
    def test_simple_query_db(self):
        result = tests.simple_query_db(sql="SELECT * FROM tabs", filename=self.test_file)
        expected_result = [(1, 'All Tasks', '/'), (2, 'Add a Task', '/add-task'), (3, 'All Categories', '/categories'), (4, 'Add a Category', '/add-category')]

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main(verbosity=1)



