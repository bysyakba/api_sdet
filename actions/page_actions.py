from playwright.sync_api import Page, expect
import allure

from constants.hosts import BASE_URL


class PageActions:
    def __init__(self, page: Page):
        self._endpoint = ""
        self._base_url = BASE_URL
        self.page = page

    @property
    def page_url(self):
        return self._base_url + self._endpoint

    @page_url.setter
    def page_url(self, endpoint):
        self._endpoint = endpoint

    def navigate(self, url):
        with allure.step(f"Переход на URL: {url}"):
            self.page.goto(url)

    def check_url(self, expected_url):
        with allure.step(f"Проверка URL: ожидаемый URL - {expected_url}"):
            expect(self.page).to_have_url(expected_url)

    def wait_for_url_change(self, expected_url):
        with allure.step(f"Ожидание изменения URL на {expected_url}"):
            print(self.page.url)
            self.page.wait_for_url(expected_url, timeout=3100000)

    def wait_for_page_load(self):
        with allure.step(f"Ожидание загрузки страницы"):
            self.page.wait_for_load_state('load', timeout=180000)

    def click_button(self, selector):
        with allure.step(f"Клик по эдементу: {selector}"):
            self.page.click(selector)

    def is_element_present(self, selector):
        with allure.step(f"Проверка видимости элемента: {selector}"):
            expect(self.page.locator(selector)).to_be_visible()

    def is_button_active(self, selector):
        with allure.step(f"Проверка активности кнопки: {selector}"):
            expect(self.page.locator(selector)).to_be_enabled()

    def input_text(self, selector, text):
        with allure.step(f"ввод текста '{text}' в элемент: {selector}"):
            self.page.fill(selector, text)

    def input_filtred_text(self, selector, text):
        with allure.step(f"ввод текста 'FILTRED' в элемент: {selector}"):
            self.page.fill(selector, text)

    def wait_for_selector(self, selector):
        with allure.step(f"Ожидаем повяления селектора: {selector}"):
            self.page.wait_for_selector(selector, state='visible')

    def wait_for_disappear_selector(self, selector):
        with allure.step(f"Ожидаем исчезновения селектора: {selector}"):
            self.page.wait_for_selector(selector, state='detached')

    def assert_text_present_on_page(self, text):
        with allure.step(f"Проверка наличия текста '{text}'на странице"):
            expect(self.page).to_have_text(text)

    def assert_text_in_element(self,selector, text):
        with allure.step(f"Проверка наличия текста '{text}'в элементк {selector}"):
            expect(self.page).locator(selector).to_have_text(text)

    def assert_element_attribute(self, selector, attribute, value):
        with allure.step(f"Проверка значения '{value}' атрибута '{attribute}' элемента: {selector}"):
            expect(self.page).locator(selector).to_have_attribute(attribute, value)

    def assert_element_hidden(self, selector):
        with allure.step(f"Проверка, что элемент {selector} скрыт"):
            expect(self.page).locator(selector).to_be_hidden()

    def activate_checkbox_if_not_active(self, selector):
        with allure.step(f"Активация чекбокса: {selector}"):
            if not self.page.is_checked(selector):
                self.page.click(selector)
                assert self.page.is_checked(selector), f"Чекбокс {selector} не получилось активировать"

    def wait_disappear_selector(self, selector, timeout=30000):
        with allure.step(f"Ожидание исчезновения лоадера: {selector}"):
            self.page.wait_for_selector(selector, state="detached", timeout=timeout)

