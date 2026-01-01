from playwright.sync_api import Playwright
def test_headers_in_response(playwright: Playwright):
    request_context =playwright.request.new_context()
    response = request_context.get("https://www.google.com")
    assert response.ok
    assert response.status==200

    headers = response.headers

    for key,value in headers.items():
        print(f"{key} ===> {value}")
    # validate header values
    assert "text/html" in headers.get("content-type")
    assert headers.get("content-encoding") == "gzip"

    # validate specific header present in response
    assert "server" in headers
    assert "content-type" in headers

