
# def test_home_page(client, create_user):
#     user = create_user(email='test@example.com', username='testuser', password='password123')
#     response = client.post('/login', data={'email': None, 'password': 123}, follow_redirects=False)
#     assert response.code == 200
#     response = client.get('/', redirect=False)
#     assert response.status_code != 200

# def test_create_post(client, create_user):
#     user = None  
#     response = client.post('/create-post', data={'text': 12345}, follow_redirects=False)
#     assert response.status_code == 200  # Fixed the status code check to integer

def test_create_post_validation(client, create_user):
    user = create_user(email='test@example.com', username='testuser', password='password123')
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    response = client.post('/create-post', data={'text': ''})
    long_text = 'a' * 1001
    response = client.post('/create-post', data={'text':long_text})

def test_delete_post(client, create_user):
     user = create_user(email='test@example.com', username='testuser', password='password123')
     response = client.post('/delete-post', data={'post_id': 'not-an-id'})
     assert response.status_code == 200
     response = client.get('/delete-post/')
#     assert b'Post deleted!' not in response  

# def test_create_comment(client, create_user):
#     user = create_user()  
#     client.get('/login', data={'email': 'test@example.com', 'password': 'password123'})
#     response = client.post('/create-comment', data={'text': None})
#     assert response.status_code == 400  # Checking for validation error for None value

# def test_like_post(client, create_user):
#     user = create_user(email='test@example.com', username='testuser', password='password123')
#     response = client.post('/like-post', data={})
#     assert response.status_code == 200  # Fixed comparison operator to ==
#     response = client.post('/like-post/1', follow_redirects=True)  # Changed client.like to client.post
#     assert response.data in user 
