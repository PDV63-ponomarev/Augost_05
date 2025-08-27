import requests
import pytest
import allure

@allure.story('Posts')
@pytest.fixture()
def num():
    return 3

@allure.feature('Manipulate posts')
@allure.story('Example')
def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')

@allure.feature('Print')
@allure.story('Example')
def test_num(num):
    print(num)


