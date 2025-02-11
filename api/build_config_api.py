from http import HTTPStatus
from custom_requester.custom_requester import CustomRequester
import json

class BuildConfigAPI(CustomRequester):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def create_build_config(self, build_config_data, expected_status=HTTPStatus.OK):
        """Создать конфигурацию сборки"""

        # print("REQUEST PAYLOAD:", json.dumps(build_config_data, indent=4))

        return self.send_request("POST", "/app/rest/buildTypes", data=build_config_data, expected_status=expected_status)

    def get_build_config_by_locator(self, locator, expected_status=HTTPStatus.OK):
        """Получить конфигурацию сборки по локатору"""
        return self.send_request("GET", f"/app/rest/buildTypes/{locator}", expected_status=expected_status)

    def delete_build_config(self, build_config_id, expected_status=HTTPStatus.NO_CONTENT):
        """Удалить конфигурацию сборки по ID"""
        return self.send_request("DELETE", f"/app/rest/buildTypes/id:{build_config_id}", expected_status=expected_status)
