import allure
import pytest
import requests
from playwright.sync_api import BrowserContext

from api.api_manager import ApiManager
from constants.browser import BROWSERS
from data.project_data import ProjectData
from data.user_data import UserData
from entities.user import User, Role
from resources.user_creds import SuperAdminCreds
from utils.browser_setup import BrowserSetup


@pytest.fixture
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = ApiManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()


@pytest.fixture
def super_admin(user_session):
    new_session = user_session()
    super_admin = User(SuperAdminCreds.USERNAME, SuperAdminCreds.PASSWORD, new_session, ["SUPER_ADMIN"])
    super_admin.api_manager.auth_api.auth_and_get_csrf(super_admin.creds)
    return super_admin

@pytest.fixture
def super_admin_creds():
    return SuperAdminCreds.USERNAME, SuperAdminCreds.PASSWORD


@pytest.fixture
def user_create(user_session, super_admin):
    created_users_pool = []

    def _user_create(role):
        user_data = UserData.create_user_data(role, scope="g")
        super_admin.api_manager.user_api.create_user(user_data)
        new_session = user_session()
        created_users_pool.append(user_data['username'])
        return User(user_data['username'], user_data['password'], new_session, [Role(role)])

    yield _user_create

    for username in created_users_pool:
        super_admin.api_manager.user_api.delete_user(username)


@pytest.fixture
def project_data(super_admin):
    project_id_pool = []

    def _project_data():
        project = ProjectData.create_project_data()
        project_id_pool.append(project.id)
        return project

    yield _project_data

    for project_id in project_id_pool:
        super_admin.api_manager.project_api.clean_up_project(project_id)


@pytest.fixture(params=BROWSERS)
def browser(request):
    plawright, browser, context, page = BrowserSetup.setup(browser_type=request.param)
    yield page
    BrowserSetup.teardown(context, browser, plawright)


@pytest.fixture(scope="function", autouse=True)
def record_video_and_screenshots(browser_context: BrowserContext, request):
    video_path = f"results/videos/{request.node.name}.webm"
    screenshot_path = f"results/screenshots/{request.node.name}.png"

    # Включаем запись видео и скриншотов
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    # Сохраняем видео и скриншот после теста
    page = browser_context.pages[0]
    page.screenshot(path=screenshot_path)
    browser_context.tracing.stop(path=video_path)

    # Прикрепляем к Allure
    allure.attach.file(video_path, name="Test Video", attachment_type=allure.attachment_type.WEBM)
    allure.attach.file(screenshot_path, name="Test Screenshot", attachment_type=allure.attachment_type.PNG)