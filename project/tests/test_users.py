import json

from project.tests.base import BaseTestCase
from project.api.models import User
from project import db


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


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
        """Ensure error is thrown if the JSON object
         does not have a username key."""
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

    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/users/foo')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exists', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/1000')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exists', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Ensure get single user behaves correctly."""
        user = add_user('tom', 'tom@foo.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data'])
            self.assertIn('success', data['status'])
            self.assertIn('tom', data['data']['username'])
            self.assertIn('tom@foo.com', data['data']['email'])

    def test_all_user(self):
        """Ensure get all users behaves correctly."""
        add_user('tom', 'tom@foo.com')
        add_user('jerry', 'jerry@foo.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data']['users'][0])
            self.assertTrue('created_at' in data['data']['users'][1])
            self.assertIn('success', data['status'])
            self.assertIn('tom', data['data']['users'][0]['username'])
            self.assertIn('tom@foo.com', data['data']['users'][0]['email'])
            self.assertIn('jerry', data['data']['users'][1]['username'])
            self.assertIn('jerry@foo.com', data['data']['users'][1]['email'])
