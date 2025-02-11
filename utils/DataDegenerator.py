import random
import string
from faker import Faker

faker_instance = Faker()

class DataGenerator:
    """
    Фейкер для генерации рандомных данных или значений
    """
    @staticmethod
    def fake_project_id():
        first_letter = faker_instance.random.choice(string.ascii_letters)
        rest_characters = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=10))
        project_id = first_letter + rest_characters
        return project_id

    @staticmethod
    def fake_name():
        return faker_instance.word()

    @staticmethod
    def fake_vcs_root_id():
        return "vcs-" + ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=8))

    @staticmethod
    def fake_step_name():
        return faker_instance.word().capitalize() + " Step"

    @staticmethod
    def fake_trigger_type():
        return faker_instance.random.choice(["vcsTrigger", "scheduleTrigger", "finishBuildTrigger"])

    @staticmethod
    def fake_properties():
        return {faker_instance.word(): faker_instance.word() for _ in range(3)}

    @staticmethod
    def fake_build_config_id():
        prefix = faker_instance.random.choice(["build", "cfg", "bc"])
        unique_part = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=8))
        return f"{prefix}{unique_part}"

    @staticmethod
    def fake_description():
        return faker_instance.sentence(nb_words=10)

    @staticmethod
    def fake_checkout_rules():
        return f"+:.=>{faker_instance.word()}"

    @staticmethod
    def fake_template_id() -> str:
        """Генерирует случайный ID шаблона в формате tmpl-XXXXX"""
        return "tmpl-" + "".join(random.choices(string.ascii_letters + string.digits, k=8))
