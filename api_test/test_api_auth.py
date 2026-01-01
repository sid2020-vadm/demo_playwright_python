import base64

import pytest
from openai import api_key
from playwright.sync_api import Playwright

#1Basic Auth
# def test_basic_auth(playwright:Playwright):
#     request_context =playwright.request.new_context()
#
#     credentials =base64.b64encode(b"user:pass").decode("utf-8")
#
#     response =request_context.get("http://httpbin.org/basic-auth/user/pass",
#                                   headers={"Authorization":f"Basic {credentials}"})
#
#     assert response.status==200
#     response_body=response.json()
#     print(response_body)
#
#     request_context.dispose()


#2Basic Auth
# def test_basic_auth(playwright:Playwright):
#     request_context =playwright.request.new_context()
#
#     credentials =base64.b64encode(b"admin:admin").decode("utf-8")
#
#     response =request_context.get("http://the-internet.herokuapp.com/basic_auth",
#                                   headers={"Authorization":f"Basic {credentials}"})
#
#     assert response.status==200
#     response_body=response.text()
#     print(response_body)
#
#     request_context.dispose()

#3 Bearer token authentication
# def test_bearer_token_auth_github_repos(playwright:Playwright):
#     context = playwright.request.new_context()
#     token = "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"
#     response = context.get("https://api.github.com/user/repos",
#                            headers={"Authorization":f"Bearer {token}"})
#     response_body = response.json()
#     assert response.ok
#     assert response.status==200
#
#     print("list of repos ",response_body )

#4 Bearer token authentication
def test_bearer_token_auth_github_repos(playwright:Playwright):
    context = playwright.request.new_context()
    token = "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"
    response = context.get("https://api.github.com/user",
                           headers={"Authorization":f"Bearer {token}"})
    response_body = response.json()
    assert response.ok
    assert response.status==200
    print("list of repos ",response_body )

# 5 API key auth
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# def test_token_key(playwright:Playwright):
#     context = playwright.request.new_context()
#     apikey = ""
#     query_params={"q":"Dehli","appid":f"{apikey}"}
#     response = context.get("https://api.openweathermap.org/data/2.5/weather",
#                            params=query_params)
#     response_body = response.json()
#     assert response.ok
#     assert response.status==200
#     print("weather report :  ",response_body )

# 6 OAuth 2 auth
def test_verify_oauth2_authentication(playwright:Playwright):
    context = playwright.request.new_context()
    client_id = None
    client_secret = None
    redirect_url = None
    grant_type = None
    authorization_code = None

    token_response = context.post("url",
                                  form={
                                      "client_id":client_id,
                                      "client_secret":client_secret,
                                      "code":authorization_code,
                                      "redirect_url":redirect_url,
                                      "grant_type":grant_type}
                                  )

    assert token_response.status==200
    token_data = token_response.json()
    access_token = token_data("access_tpken")
    print(f"Access token : {access_token}")

    assert access_token is not None

    imgur_response = context.get(
        "url",
        headers={"Authorization":f"Bearer {access_token}"}
    )
    assert imgur_response.ok
    imgur_response_body = imgur_response.json()
    print(imgur_response_body)


    context.dispose()
