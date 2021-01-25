import time


def test_guest_should_see_login_link(browser):
    browser.get("http://selenium1py.pythonanywhere.com/")
    time.sleep(3)
    browser.find_element_by_id("login_link").click()
    time.sleep(3)
