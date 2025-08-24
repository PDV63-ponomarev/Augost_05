import requests 

# def all_posts():
#     # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
#     ## OR
#     response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
#     assert len(response) == 99, 'Not all posts returned' 
#     # проверка 100 ли постов, если все верно ответа не будет


# all_posts()


####################################


# def one_post():
#     post_id = 42
#     response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
#     assert response['id'] == post_id
# # проверка равен ли id ссылке

# one_post()


####################################


def post_a_post():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    
    headers = {'Content-type': 'application/json'}

    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json = body,
        headers = headers
    )

    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'ID is incorrect'

post_a_post()


################


# def put_a_post():
#     body = {
#         'title': 'foo-UOO',
#         'body': 'bar-UPD',
#         'userId': 13
#     }
    
#     headers = {'Content-type': 'application/json'}

#     response = requests.put(
#         'https://jsonplaceholder.typicode.com/posts/33',
#         json = body,
#         headers = headers
#     ).json()

#     print(response)

# put_a_post()


################


# def path_a_post():
#     body = {
#         'body': 'bar-UPD',
#         'userId': 12
#     }
    
#     headers = {'Content-type': 'application/json'}

#     response = requests.put(
#         'https://jsonplaceholder.typicode.com/posts/33',
#         json = body,
#         headers = headers
#     ).json()

#     print(response)

# path_a_post()


################

# def delete_a_post():
#     response = requests.delete('https://jsonplaceholder.typicode.com/posts/33')
#     print(response.json())
#     print(response.status_code)

# delete_a_post()
