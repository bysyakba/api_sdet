from typing import Optional, Dict, List
from pydantic import BaseModel

from utils.DataDegenerator import DataGenerator


class VcsRootEntryModel(BaseModel):
    id: str
    checkoutRules: Optional[str] = None


class PropertyModel(BaseModel):
    name: str
    value: str


class StepModel(BaseModel):
    name: str
    type: str
    properties: Dict[str, List[PropertyModel]]


class TriggerModel(BaseModel):
    type: str
    properties: Dict[str, str]


class TemplateModel(BaseModel):
    id: str


class BuildConfigDataModel(BaseModel):
    id: str
    name: str
    project: Dict[str, str]
    templates: Optional[Dict[str, List[TemplateModel]]] = None
    parameters: Optional[Dict[str, List[PropertyModel]]] = None
    # vcsRootEntries: Optional[List[VcsRootEntryModel]] = None
    steps: Optional[Dict[str, List[StepModel]]] = None
    # triggers: Optional[List[TriggerModel]] = None


class BuildConfigData:
    @staticmethod
    def create_build_config_data(project_id: str) -> BuildConfigDataModel:
        return BuildConfigDataModel(
            id=DataGenerator.fake_build_config_id(),
            name=DataGenerator.fake_name(),
            project={"id": project_id},
            templates={
                "buildType": [
                    TemplateModel(id=DataGenerator.fake_template_id())
                ]
            },
            parameters={
                "property": [
                    PropertyModel(name="myBuildParameter", value="myValue")
                ]
            },
            steps={
                "step": [
                    StepModel(
                        name=DataGenerator.fake_step_name(),
                        type="simpleRunner",
                        properties={
                            "property": [
                                PropertyModel(name="script.content", value="echo 'Hello World!'")
                            ]
                        }
                    )
                ]
            }
        )


class BuildConfigResponseModel(BaseModel):
    id: str
    name: str
    projectId: str
    description: Optional[str] = None
    href: str
    webUrl: str
    steps: Optional[Dict[str, List[StepModel]]] = None
    triggers: Optional[List[TriggerModel]] = None
    vcsRootEntries: Optional[List[VcsRootEntryModel]] = None

    class Config:
        extra = "allow"
