from constants.roles import Roles
from data.project_data import ProjectData, ProjectResponseModel


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_data_id = cls.project_data.id


    def test_create_project_with_role(self, super_admin, project_data):
        project_data_1 = project_data()
        project_data_2 = project_data()
        response = super_admin.api_manager.project_api.create_project(project_data_1.model_dump()).text
        project_response = ProjectResponseModel.model_validate_json(response)
        assert project_response.id == project_data_1.id, \
            f"expected project id= {project_data_1.id}, but '{project_response.id}' given"
        assert project_response.parentProjectId == project_data_1.parentProject["locator"], \
            (f"expected parent project id= {project_data_1.parentProject['locator']},"
             f" but '{project_response.parentProjectId}' given in response")

        response = super_admin.api_manager.project_api.create_project(project_data_2.model_dump()).text
        project_response = ProjectResponseModel.model_validate_json(response)
        assert project_response.id == project_data_2.id, \
            f"expected project id= {project_data_2.id}, but '{project_response.id}' given"
        assert project_response.parentProjectId == project_data_2.parentProject["locator"], \
            (f"expected parent project id= {project_data_2.parentProject['locator']},"
             f" but '{project_response.parentProjectId}' given in response")