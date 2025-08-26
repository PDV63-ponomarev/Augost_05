import requests
import pytest


@pytest.fixture() # отрабатывает в функциях где его обьявят
def new_post_id():
    body = {"title": "fsak",  "body": "baras", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    post_id = response.json()['id']
    print(post_id)
    yield post_id # все что после отработает после теста
    print('Deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture()
def num():
    return 1