import allure

from data.project_data import ProjectResponseModel
from pages.create_project_page import ProjectCreationPage


def test_create_project(browser, project_data, super_admin):
    project_data_1 = project_data()
    project_id = project_data_1.id
    project_name = project_data_1.name

    with allure.step("Авторизация пользователя"):
        browser.goto('http://localhost:8111/login.html')
        browser.fill('#username', 'admin')
        browser.fill('#password', 'lox')
        browser.click('.loginButton')
        browser.wait_for_url('http://localhost:8111/favorite/projects?mode=builds')
    with allure.step("Создание проекта"):
        project_creation_browser = ProjectCreationPage(browser)
        project_creation_browser.create_project(project_name, project_id, project_name)
    with allure.step('Отправка запроса на получение информации созданного проекта'):
        response = super_admin.api_manager.project_api.get_project_by_locator(project_data_1.name).text
        created_project = ProjectResponseModel.model_validate_json(response)
        assert created_project.id == project_data_1.id, \
            f"expected project id= {project_data_1.id}, but '{created_project.id}' given"