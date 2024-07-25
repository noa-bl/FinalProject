import sys
import os
import pytest
from unittest.mock import patch, MagicMock


# Adjust the sys.path to include the /app directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import app, signup, index, newPost, getUpdatedPosts, allPosts

# Test data
mock_user = {
    'username': 'nonexistentuser',
    'password': 'password'
}

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_login_failure(client):
    # Mocking the behavior inside the index function instead of the function itself
    with patch('app.Users.find_one') as mock_find_one:
        mock_find_one.return_value = None  # Simulate nonexistent user
        
        response = client.post('/', data={
            'username': 'nonexistentuser',
            'password': 'password'
        })
        assert b"Failed Login" in response.data


def test_login_success(client):
    # Mocking the behavior inside the index function instead of the function itself
    with patch('app.Users.find_one') as mock_find_one, \
         patch('app.Posts.find') as mock_find_posts, \
         patch('app.Posts.count_documents') as mock_count_documents, \
         patch('app.render_template') as mock_render_template:

        # Mock the return values
        mock_find_one.return_value = {'username': 'usertest', 'password': 'passwordtest'}
        mock_find_posts.return_value = [
            {'title': 'Test Post', 'content': 'This is a test post.', 'likes': [], '_id': 'some_id'}
        ]
        mock_count_documents.return_value = 1
        mock_render_template.return_value = "Rendered Template"  # Mock render_template response

        # Use the correct credentials to test a successful login
        response = client.post('/', data={
            'username': 'usertest',
            'password': 'passwordtest'
        })

        # Check for a successful login
        assert response.status_code == 200
        assert b"Failed Login" not in response.data
        
        # Verify render_template was called with the correct parameters
        mock_render_template.assert_called_once_with(
            'userPage.html', 
            postsNum=1, 
            user_posts_list=[
                {'title': 'Test Post', 'content': 'This is a test post.', 'likes': [], '_id': 'some_id'}
            ], 
            username='usertest'
        )

from unittest.mock import patch, MagicMock

def test_new_post(client):
    # Mocking the behavior inside the newPost function instead of the function itself
    with patch('app.Posts.find_one') as mock_find_one, \
         patch('app.Posts.insert_one') as mock_insert_one, \
         patch('app.Posts.find') as mock_find_posts, \
         patch('app.Posts.count_documents') as mock_count_documents, \
         patch('app.render_template') as mock_render_template:

        # Mock the return values
        mock_find_one.return_value = None  # No existing post
        mock_find_posts.return_value = [
            {'title': 'Test Post', 'content': 'This is a test post.', 'likes': [], '_id': 'some_id'}
        ]
        mock_count_documents.return_value = 1
        mock_render_template.return_value = "Rendered Template"  # Mock render_template response

        # Simulate a session with a logged-in user
        with client.session_transaction() as sess:
            sess['username'] = 'usertest'

        # Use the correct data to test creating a new post
        response = client.post('/newPost', data={
            'title': 'Test Post',
            'content': 'This is a test post.'
        })

        # Check for a successful new post creation
        assert response.status_code == 200
        assert b"Title, content, or username not provided" not in response.data
        assert b"Post already exists" not in response.data
        
        # Verify render_template was called with the correct parameters
        mock_render_template.assert_called_once_with(
            'userPage.html', 
            postsNum=1, 
            user_posts_list=[
                {'title': 'Test Post', 'content': 'This is a test post.', 'likes': [], '_id': 'some_id'}
            ], 
            username='usertest'
        )
