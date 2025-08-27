import requests
import pytest
import allure



@pytest.fixture(scope='session')
# первая часть отрабатывает где обьявили, последняя вконце последнего теста
# используется например для коннекта с бд
# выполняется только 1 раз
def hello():
    print('HELLO')
    yield
    print('BYE')


@allure.feature('Get posts')
@allure.story('Posts')
# @pytest.mark.skip('No preconditions')
def test_get_one_post(new_post_id, hello):
    print('test')
    with allure.step(f'Run get request for post {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step('Chec that post id is {new_post_id}'):
        assert response['id'] == {11}


@allure.feature('Get posts')
@allure.story('Posts')
@pytest.mark.smoke
def test_get_all_posts(hello):
    print('test')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response), 100


@allure.feature('Manipulate posts')
@allure.story('Posts')
@pytest.mark.regression
def test_add_post():
    print('test')
    with allure.step('Prepare test date'):
        body = {
            "title": "fsak",
            "body": "baras",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run requesr to create a post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 201'):
        assert response.status_code == 201
    with allure.step('Check response code is 101'):
        assert response.json()['id'] == 101


@allure.feature('equals')
@allure.story('Example')
@pytest.mark.smoke
def test_one():
    assert 1 == 1

@allure.feature('equals')
@allure.story('Example')
@pytest.mark.regression
def test_two():
    assert 2 == 2

@allure.feature('equals')
@allure.story('Example')
@pytest.mark.parametrize('logins', ['', ' ', '()@#$%^&*~', '1234']) 
# запустится столько раз, сколько параметров задано
def test_three(logins):
    print(logins)
    assert 3 == 3

@allure.feature('equals')
@allure.story('Example')
@pytest.mark.smoke
def test_four():
    assert 4 == 4