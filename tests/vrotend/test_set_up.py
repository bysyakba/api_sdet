import allure

from conftest import browser
from pages.setup_page import SetUpPage


@allure.title("sepup of server")
@allure.description("setup proj and agree user agreement")
def test_set_up(browser):
    with allure.step("Setup"):
        set_up_page = SetUpPage(browser)

        set_up_page.set_up()