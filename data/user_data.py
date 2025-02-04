from constants.roles import Roles
from utils.DataDegenerator import DataGenerator


class UserData:
    @staticmethod
    def create_user_data(role=Roles.SYSTEM_ADMIN.value, scope="g"):
        return {
                "username": DataGenerator.fake_name(),
                "password": DataGenerator.fake_project_id(),
                "email": "example@email.com",
                "roles": {
                    "role": [
                        {
                            "roleId": role,
                            "scope": scope,
                        }
                    ]
                }
        }