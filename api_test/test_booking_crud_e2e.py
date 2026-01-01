import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright

# global variables
base_url = "https://restful-booker.herokuapp.com"
booking_id =None
token = None

#utility function -- read json file
def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

#fixture -- create playwright context
@pytest.fixture(scope="session")
def api_context(playwright:Playwright):
    context= playwright.request.new_context()
    yield context
    context.dispose()

#1.create booking
def test_create_booking(api_context):
    request_data = read_json("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\post_request_body.json")
    response =api_context.post(f"{base_url}/booking",data=request_data)
    assert response.ok, "POST request failed"
    assert response.status==200
    response_body =response.json()
    print(response_body)
    assert "bookingid" in response_body
    global booking_id # global variable
    booking_id = response_body["bookingid"]
    print(f"booking id  : {booking_id}")

#2.Get booking details By ID, Name,Checkin and Checkout
def test_get_booking_by_id(api_context):
    response = api_context.get(f"{base_url}/booking/{booking_id}") # https://restful-booker.herokuapp.com/booking/1
    assert response.ok
    assert  response.status==200
    response_body= response.json()
    print(f"Booking details by id {booking_id} : ",response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body

def test_get_booking_by_name(api_context):
    # https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown
    name_query_params ={"firstname":"Agra","lastname":"Badami"}
    response = api_context.get(f"{base_url}/booking",
                               params=name_query_params)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Booking  ids {name_query_params} : ", response_body)

    assert len(response_body) >0

def test_get_booking_by_dates(api_context):
    date_query_params ={"checkin":"2018-06-01","checkout":"2018-08-01"}
    # https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21
    response = api_context.get(f"{base_url}/booking",params=date_query_params)
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print(f"Booking  ids {date_query_params} : ", response_body)

#3 create token
def test_create_token(api_context):
    request_data = read_json("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\/token_request_body.json")
    response = api_context.post(f"{base_url}/auth",data=request_data)

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    assert "token" in response_body
    print("Token creation :",response_body)
    global  token #global variable
    token = response_body["token"]
    assert len(token)>5

#4 partial update
def test_partial_update_booking(api_context):
    request_data = read_json("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\patch_booking_update.json")
    response = api_context.patch(f"{base_url}/{booking_id}",
                                 headers={"Cookie":f"token={token}"},
                                 data=request_data)

    assert response.ok
    assert response.status==200
    response_body = response.json()
    print("Partial updateresponse :",response_body)


#5 put / full update request
def test_update_booking(api_context):
    request_data = read_json("E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\put_request_body.json")
    response = api_context.put(f"{base_url}/booking/{booking_id}",headers={"Cookie":f"token={token}"},
                                 data=request_data)

    assert  response.ok
    assert  response.status==200
    response_body = response.json()
    print("Full update response : ",response_body )

#6 delete booking
def test_delete_booking(api_context):
    response = api_context.put(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={token}"})
    assert response.ok
    assert response.status == 201













