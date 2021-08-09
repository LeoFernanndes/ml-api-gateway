import fastapi
from pydantic import BaseModel, Field
from models.titanic_predictor import IrisPredictorV1


router = fastapi.APIRouter()

class TitanicData(BaseModel):
    pclass: float = Field(...)
    sex: float = Field(...)
    age: float = Field(...)
    subsp: float = Field(...)
    parch: float = Field(...)
    age: float = Field(...)
    subsp: float = Field(...)


@router.post('/')
async def classify_flower(payload: TitanicData):



    predictor = IrisPredictorV1()
    flower_data_dict = dict(payload)
    flower_data = [flower_data_dict[key] for key in flower_data_dict.keys()]
    prediction = predictor.predict(flower_data)
    return prediction

@router.get("/")
async def classify_flower():
    return "api/v1/titanic/"