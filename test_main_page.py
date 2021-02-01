import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(3)


@pytest.mark.regression
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_login_link()


@pytest.mark.smoke
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_login_form()


@pytest.mark.smoke
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_register_form()


@pytest.mark.smoke
def test_login_should_be_presented_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_login_url()
