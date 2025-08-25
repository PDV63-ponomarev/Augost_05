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


@pytest.fixture(scope='session')
# первая часть отрабатывает где обьявили, последняя вконце последнего теста
# используется например для коннекта с бд
# выполняется только 1 раз
def hello():
    print('HELLO')
    yield
    print('BYE')




# @pytest.mark.skip('No preconditions')
def test_get_one_post(new_post_id):
    print('test')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.smoke
def test_get_all_posts(hello):
    print('test')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response), 100


@pytest.mark.regression
def test_add_post():
    print('test')
    body = {
        "title": "fsak",
        "body": "baras",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()['id'] == 101


@pytest.mark.smoke
def test_one():
    assert 1 == 1

@pytest.mark.regression
def test_two():
    assert 2 == 2

@pytest.mark.parametrize('logins', ['', ' ', '()@#$%^&*~']) 
# запустится столько раз, сколько параметров задано
def test_three(logins):
    print(logins)
    assert 3 == 3

@pytest.mark.smoke
def test_four():
    assert 4 == 4