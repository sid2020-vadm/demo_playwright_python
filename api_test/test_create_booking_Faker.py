import datetime
import json
from datetime import timedelta

from faker import Faker
from playwright.sync_api import Playwright, expect


def test_create_booking(playwright: Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(min=100, max=5000)
    deposit_paid = faker.boolean()
    addtionalneeds = faker.word()
    checkin_date = datetime.date.today().strftime("%Y-%m-%d")
    checkout_date = (datetime.date.today()+timedelta(days=5)).strftime("%Y-%m-%d")

    request_body ={
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin_date,
            "checkout": checkout_date
        },
        "additionalneeds": addtionalneeds
    }

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
    assert booking["firstname"] == first_name
    assert booking["lastname"] == last_name
    assert booking["totalprice"] == total_price
    assert booking["depositpaid"] == deposit_paid
    assert booking["additionalneeds"] == addtionalneeds
    assert booking["bookingdates"]["checkin"]==checkin_date
    assert booking["bookingdates"]["checkout"] == checkout_date

    request_context.dispose()




