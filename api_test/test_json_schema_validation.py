from jsonschema import validate
from playwright.sync_api import Playwright
from pydantic import ValidationError
# pip install jsonschema

myschema = {
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "city": {
      "type": "string"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "firstName",
    "lastName",
    "city",
    "state"
  ]
}

def test_json_schema_validation(playwright:Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://mocktarget.apigee.net/json")
    assert response.ok
    response_body = response.json()

    print("response body :" ,response_body)
    try:
        validate(instance=response_body,schema=myschema)
        print("schema validation successfully")

    except ValidationError as e:
        print("schema validation failed",e)

    request_context.dispose()




