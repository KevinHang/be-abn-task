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
        db.create_all()
        # Add a sample TV show for testing retrieve and delete operations
        self.sample_tv_show = {'name': 'Sample Show', 'genre': 'Sample Genre'}
        response = self.client.post('/tvshows', data=json.dumps(self.sample_tv_show), content_type='application/json')
        self.sample_tv_show_id = json.loads(response.data).get('id')
        print("\nSetup complete.")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        print("Teardown complete. Database cleared.")

    def test_create_tv_show(self):
        print("Testing: Create a new TV show...")
        response = self.client.post('/tvshows', data=json.dumps({'name': 'New Show', 'genre': 'Drama'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        print("Test passed: New TV show created successfully.")

    def test_get_all_tv_shows(self):
        print("Testing: Retrieve all TV shows...")
        response = self.client.get('/tvshows')
        self.assertEqual(response.status_code, 200)
        print("Test passed: All TV shows retrieved successfully.")

    def test_get_single_tv_show(self):
        print("Testing: Retrieve a single TV show by its ID...")
        response = self.client.get(f'/tvshows/{self.sample_tv_show_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Show', response.data.decode())
        print("Test passed: Single TV show retrieved successfully by its ID.")

    def test_search_tv_show_by_genre(self):
        print("Testing: Search TV show by genre...")
        response = self.client.get(f'/tvshows/search/Sample Genre')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Show', response.data.decode())
        print("Test passed: TV show searched by genre successfully.")

    def test_update_tv_show(self):
        print("Testing: Update an existing TV show...")
        response = self.client.put(f'/tvshows/{self.sample_tv_show_id}', data=json.dumps({'name': 'Updated Show', 'genre': 'Updated Genre'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_response = self.client.get(f'/tvshows/{self.sample_tv_show_id}')
        self.assertIn('Updated Show', updated_response.data.decode())
        print("Test passed: Existing TV show updated successfully.")

    def test_delete_tv_show(self):
        print("Testing: Delete a TV show by its ID...")
        response = self.client.delete(f'/tvshows/{self.sample_tv_show_id}')
        self.assertEqual(response.status_code, 200)
        follow_up_response = self.client.get(f'/tvshows/{self.sample_tv_show_id}')
        self.assertEqual(follow_up_response.status_code, 404)
        print("Test passed: TV show deleted by its ID successfully.")

if __name__ == '__main__':
    unittest.main()
