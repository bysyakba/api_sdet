import random
import time

import allure

from constants.browser import VALUE
from pages.create_build_config_page import BuildCreationPage
from pages.create_project_page import ProjectCreationPage


def test_create_build_config(browser, project_data, super_admin):
    project_data_1 = project_data()
    project_id = project_data_1.id
    project_name = project_data_1.name

    with allure.step("Авторизация пользователя"):
        browser.goto('http://localhost:8111/login.html')
        browser.fill('#username', 'admin')
        browser.fill('#password', 'lox')
        browser.click('.loginButton')
        # browser.wait_for_selector('#errorMessage')
        # time.sleep(5)
        browser.wait_for_url('http://localhost:8111/favorite/projects', timeout=1000000000)
        # time.sleep(5)

    with allure.step("Создание проекта"):
        project_creation_browser = ProjectCreationPage(browser)
        project_creation_browser.create_project(project_name, project_id, project_name)
    with allure.step("Создание билд конфига"):
        build_creation_browser = BuildCreationPage(browser)
        build_creation_browser.create_build(project_name, project_id, project_name)
        [browser.type('#artifactPaths', x, delay=random.randint(50, 700)) for x in VALUE]
        time.sleep(2)