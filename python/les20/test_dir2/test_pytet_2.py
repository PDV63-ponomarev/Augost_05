import requests
import pytest

@pytest.fixture()
def num():
    return 3

def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')

def test_num(num):
    print(num)


# pip install pytest-xdist  
# установка pyworkera позволяюшего запустить много тестов паралельно
# pytest -v -n auto запуск с pyworkeroм, сколько ядер столько и паралельных тестов


# плагин allure нужен для визуализации результатов тестов
# pip install allure-pytest
# pytest -v --alluredir=allur-results запуск плагина. положит в паплку allur-results
# для чтения отчета нужен Java (11 или 17) и allure
 