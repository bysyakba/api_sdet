import allure
from pages.base_page import BasePage


class CreateBuildContainerFragment(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.build_name_selector = "input#buildTypeName"
        self.build_id_selector = "input#buildTypeExternalId"
        self.build_description_selector = "input#description"
        self.create_build_button = "input.submitButton"
        self.skip_url_repository = ".cancel"
        self.general_settings = "#general_Tab"


    def input_build_details(self, name, project_id, description):
        with allure.step("Ввод данных для создания билд конфига"):
            self.actions.wait_for_selector(self.build_name_selector)
            self.actions.input_text(self.build_name_selector, name)
            self.actions.input_text(self.build_id_selector, project_id)
            self.actions.input_text(self.build_description_selector, description)

    def click_create_button(self):
        with allure.step("Нажатие кнопки создания билд конфига"):
            self.actions.click_button(self.create_build_button)

    def click_skip_button(self):
        with allure.step("Нажатие кнопки пропуска урла"):
            self.actions.click_button(self.skip_url_repository)

    def click_general_settings(self):
        with allure.step("Нажатие таба general_settings"):
            self.actions.click_button(self.general_settings)


class BuildCreationPage(BasePage):
        def __init__(self, page):
            super().__init__(page)
            self.page_url = ('/admin/createObjectMenu.html?projectId=id353&showMode=createBuildTypeMenu&cameFromUrl=%2Fadmin%2FeditProject.html%3FprojectId%3Did353#createManually')
            self.create_form_container = CreateBuildContainerFragment(page)
            self.create_build_config = ".icon_before"

        def create_build_configs(self):
            with allure.step("Нажатие таба create_build_config"):
                self.actions.click_button(self.create_build_config)


        def create_build(self, name, project_id, description):
            self.create_build_configs()
            self.create_form_container.input_build_details(name, project_id, description)
            self.create_form_container.click_create_button()
            self.create_form_container.click_skip_button()
            self.create_form_container.click_general_settings()
            self.page_url = (f'/admin/editBuild.html?id=buildType:{project_id}')
            self.actions.wait_for_url_change(self.page_url)

