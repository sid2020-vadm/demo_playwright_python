from playwright.sync_api import Playwright
from pygments.styles.dracula import pink


def test_cookies_in_response(playwright:Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com")

    assert response.ok
    assert response.status==200
    # extarct cookies from response
    cookies = request_context.storage_state()["cookies"]
    print(cookies)

    for c in cookies:
        print(f"{c['name']}==>{c['value']}==>{c['domain']}")

    # check if 'AEC' cookie exist or not
    aec_cookie = None
    for c in cookies:
        if c['name'] == 'AEC':
            aec_cookie = c
            break

    assert  aec_cookie is not None ,"Cookie called 'AEC' not found"

    # print details of 'AEC' cookie
    print(aec_cookie['name'])
    print(aec_cookie['value'])
    print([aec_cookie['domain']])
    print(aec_cookie['expires'])
    print(aec_cookie['path'])