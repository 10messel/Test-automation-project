import time
import pytest
from .pages.product_page import ProductPage


@pytest.mark.smoke
@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail(reason="Expected falling")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_product_messages()
