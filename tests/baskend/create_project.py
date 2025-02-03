import requests
import pytest


BASE_URL = 'http://admin:loh@localhost:8111'


class TestProjectCreate:

    def test_project_create(self):
        # Получение токена
        auth_response = requests.get(url=f"{BASE_URL}/authenticationTest.html?csrf", auth=("admin", "loh"))
        csrf_token = auth_response.text
        headers = {"X-TC-CSRF-Token": csrf_token}

        # Подготовка данных
        project_id="simpleprojectID3"
        project_data= {
                        "parentProject": {
                                            "locator": "_Root"
                                         },
                        "name": "ProjectNameSimple3",
                        "id": project_id,
                        "copyAllAssociatedSettings": True
                      }
        # Создание проекта
        create_responce = requests.post(url=f"{BASE_URL}/app/rest/projects", headers=headers, json=project_data)
        assert create_responce.status_code == 200, "Не удалось создать проект"

        check_project = requests.get(url=f"{BASE_URL}/app/rest/projects/id:{project_id}",headers=headers)
        assert check_project.status_code == 200

        # Удаление проекта
        delete_project = requests.delete(url=f"{BASE_URL}/app/rest/projects/id:{project_id}", headers=headers)
        assert delete_project.status_code == 204, "Не удалось удалить проект"