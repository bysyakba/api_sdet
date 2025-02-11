import allure
import pytest

from data.build_config_data import BuildConfigResponseModel, BuildConfigData


class TestBuildConfigCreate:

    @allure.feature('Управление конфигурациями сборки')
    @allure.story('Создание конфигурации сборки')
    @allure.testcase('https://testcase.manager/testcase/789', name='Тест-кейс')
    @allure.title('Проверка создания конфигурации сборки')
    @allure.description('Тест проверяет создание новой конфигурации сборки и ее появление в общем списке конфигураций.')
    def test_create_build_config(self, super_admin, project):
        """Создание конфигурации сборки для заранее созданного проекта"""
        build_config_data = BuildConfigData.create_build_config_data(project)

        with allure.step('Отправка запроса на создание конфигурации сборки'):
            response = super_admin.api_manager.build_config_api.create_build_config(build_config_data.model_dump()).text
            build_config_response = BuildConfigResponseModel.model_validate_json(response)

        with pytest.assume:
            assert build_config_response.id == build_config_data.id
            assert build_config_response.projectId == project

        with allure.step("Отправка запроса на получение информации о созданной конфигурации сборки"):
            response = super_admin.api_manager.build_config_api.get_build_config_by_locator(build_config_data.name).text

        with allure.step("Проверка соответствия параметров созданной конфигурации сборки с отправленными данными"):
            created_build_config = BuildConfigResponseModel.model_validate_json(response)

        with pytest.assume:
            assert created_build_config.id == build_config_data.id, \
                f"Ожидался ID конфигурации сборки = {build_config_data.id}, но получен '{created_build_config.id}'"
