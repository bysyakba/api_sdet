import allure
# from pages.base_page import BasePage
from actions.page_actions import PageActions
from constants.hosts import BASE_URL


class FirstStartWindow(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.window_locator = "#nestedPageContent"
        self.proceed_button_locator = "#proceedButton"

    def proceed_step(self):
        with allure.step("Нажатие кнопки proceed"):
            self.click_button(self.proceed_button_locator)


class Loading(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.loading_icon_locator = ".icon-refresh"

    def wait_loading(self
                     , timeout_wait=1000000000
                     , timeout_disappear=1000000000):
        with allure.step("Ждем начала лоадинга"):
            self.wait_for_selector(self.loading_icon_locator, timeout_wait)
        with allure.step("Ждем когда закончится лоадинг"):
            self.wait_disappear_selector(self.loading_icon_locator, timeout_disappear)


class Agreement(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.page_url = "/showAgreement.html"
        self.page_setup = f"{BASE_URL}/setupAdmin.html"
        self.accept_checkbox_locator = "#accept"
        self.continue_button_locator = ".btn"

    def check_in_box(self):
        with allure.step("Активируем чекбокс"):
            self.activate_checkbox_if_not_active(self.accept_checkbox_locator)

    def continue_agreement(self):
        with allure.step("Принимаем Agreement"):
            self.click_button(self.continue_button_locator)


class SetUpUser(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_locator = "#input_teamcityUsername"
        self.password_locator = "#password1"
        self.confirm_password_locator = "#retypedPassword"
        self.create_button = ".btn"

    def fill_user_data(self, user_name, user_password):
        self.input_text(self.username_locator, user_name)
        self.input_text(self.password_locator, user_password)
        self.input_text(self.confirm_password_locator, user_password)

    def create_user(self):
        self.click_button(self.create_button)


class SetUpPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.first_start_window = FirstStartWindow(self.page)
        self.loading = Loading(self.page)
        self.agreement = Agreement(self.page)
        self.setup_user = SetUpUser(self.page)

    # def set_up2(self, username="admin", password="lox"):
    #     self.navigate(self.page_url)
    #     self.wait_for_page_load()
    #     self.first_start_window.proceed_step()
    #     self.loading.wait_loading()
    #     self.first_start_window.proceed_step()
    #     self.loading.wait_loading()
    #     self.check_url(self.agreement.page_url)
    #     self.agreement.check_in_box()
    #     self.agreement.continue_agreement()
    #     self.wait_for_url_change(self.agreement.page_url)
    #     self.wait_for_page_load()
    #     self.setup_user.fill_user_data(username, password)
    #     self.setup_user.create_user()
    #     self.wait_for_url_change(self.setup_user.page_url)


    def set_up(self, username="admin", password="lox"):
        self.navigate(self.page_url)
        self.wait_for_page_load()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.check_url(self.agreement.page_url)
        self.agreement.check_in_box()
        self.agreement.continue_agreement()
        self.wait_for_url_change(self.agreement.page_setup)
        self.wait_for_page_load()
        self.setup_user.fill_user_data(username, password)
        self.setup_user.create_user()
        self.wait_for_url_change(f"{BASE_URL}/favorite/projects")