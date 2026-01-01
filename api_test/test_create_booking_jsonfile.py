import json

from playwright.sync_api import Playwright, expect


def test_create_booking(playwright: Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()
    with open("testdata/post_request_body.json","r") as f:
        request_body = json.load(f)

    response=  request_context.post(f"{base_url}/booking",data=request_body)


    #validation
    assert response.ok
    assert  response.status ==200

    response_body= response.json()
    print(response_body)

    #  response body field/attribute validation
    assert "bookingid" in response_body
    assert  "booking" in response_body

    #data validation
    booking= response_body["booking"]
    assert booking["firstname"] == "Agra"
    assert booking["lastname"] == "Badami"
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] == True
    assert booking["additionalneeds"] == "Breakfast"
    assert booking["bookingdates"]["checkin"]=="2018-06-01"
    assert booking["bookingdates"]["checkout"] == "2018-08-01"

    request_context.dispose()




