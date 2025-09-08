from playwright.sync_api import Page, expect, Request, Response, Route
from time import sleep
import re
import json 


# def test_listen(page: Page):

#     def print_request(request:Request):
#         print('REQUEST:', request.post_data, request.url)

    
    
#     # включение отслеживание запросов, при появление отраб функцию
#     page.on('request', print_request)
#     page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
#     page.goto('https://www.qa-practice.com/')
#     sleep(2)
#     page.get_by_role('link', name = 'Text input').click()
#     input_field = page.locator('#id_text_string')
#     input_field.fill('sometext')
#     input_field.press('Enter')
#     sleep(2)




# def test_catch_response(page:Page):

#     page.goto('https://www.airbnb.ru/')
#     with page.expect_response(re.compile('messages')) as response_event: 
#         page.locator('[data-title="Впечатления"]').click()
   

#     response = response_event.value
#     print(response.url)
#     print(response.status)
#     print(response.text)
    



###################################

#подмена запроса

# def test_pogoda(page:Page):

#     def handle_route(route:Route):
#         response = route.fetch()
#         body = response.json()
#         body['temperature'] = '+10'
#         body['icon'] = 'A2'
#         body = json.dumps(body)
#         route.fulfill(
#             response=response,
#             body=body
#             )


#     def handle_route_2(route:Route):
#         url = route.request.url
#         url = url.replace('api/', '')
#         route.continue_(url=url)


#     page.route('**/pogoda/**', handle_route_2)
#     page.goto('https://www.onliner.by/')
#     sleep(20)
#     page.locator('[name="query"]').click()
#     sleep(5)



# def test_change_request(page:Page):

#     def change_req(route:Route):
#         url = route.request.url
#         print(url)
#         url = url.replace('&sort=newest','')
#         route.continue_(url=url)
#     page.route(re.compile('/product/finder'), change_req)
#     page.set_viewport_size({"width": 1920, "height": 1080})
#     page.goto('https://www.samsung.com/ru/smartphones/galaxy-z/')
#     sleep(5)
#     page.locator('[aria-label="Galaxy S"]').click()
    
   
#     sleep(5)




def test_API(page:Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/23')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 23