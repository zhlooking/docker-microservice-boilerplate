import json

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Test for the users servcie"""
    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """Ensure a new user can be added to the database"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='micheal',
                    email='micheal@foo.com'
                )),
                content_type='application/json',
            )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn('micheal@foo.com', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json',
            )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid payload', data['message'])
        self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    email='micheal@foo.com'
                )),
                content_type='application/json',
            )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('fail', data['status'])
        self.assertIn('Invalid payload', data['message'])

    def test_add_user_duplicate_user(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='john',
                    email='john@foo.com'
                )),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='john',
                    email='john@foo.com'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('fail', data['status'])
            self.assertIn('Email already exists', data['message'])
