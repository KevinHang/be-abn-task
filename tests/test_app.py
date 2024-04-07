import unittest
import json
from app import create_app
from app.extensions import db

class TVShowTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Create all database tables
        print("\nSetup complete.")

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Drop all database tables
        self.app_context.pop()  # Pop the application context
        print("Teardown complete. Database cleared.")

    # Test for creating a new tw show
    def test_create_tv_show(self):
        print("Testing: Create a new TV show...")
        response = self.client.post('/tvshows', data=json.dumps({'name': 'Test Show', 'genre': 'Test Genre'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        print("Test passed: New TV show created successfully.")

    # Test for retrieving all TV shows
    def test_get_all_tv_shows(self):
        print("Testing: Retrieve all TV shows...")
        response = self.client.get('/tvshows')
        self.assertEqual(response.status_code, 200)
        print("Test passed: All TV shows retrieved successfully.")

if __name__ == '__main__':
    unittest.main()
