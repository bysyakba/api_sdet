import time

from playwright.sync_api import sync_playwright


def test_create_project_simple(project_data, browser):
    project_data_1 = project_data()
    project_id = project_data_1.id
    project_name = project_data_1.name

    browser.goto('http://localhost:8111/login.html')
    browser.fill('#username', 'admin')
    browser.fill('#password', 'lox')
    browser.click('.loginButton')
    browser.wait_for_url('http://localhost:8111/favorite/projects?mode=builds')

    browser.goto('http://localhost:8111/admin/createObjectMenu.html?projectId=_Root&showMode=createProjectMenu')
    browser.click('text=Manually')
    browser.fill('input#name', project_name)
    browser.fill('input#externalId', project_id)
    browser.fill('input#description', 'Описание тестового проекта')
    browser.click('input.submitButton')

    browser.wait_for_url(f'http://localhost:8111/admin/editProject.html?projectId={project_id}')
    assert project_name in browser.text_content('body')

    browser.close()