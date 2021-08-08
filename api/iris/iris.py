import fastapi
from pydantic import BaseModel, Field
from models.iris_predictor import IrisPredictorV1


router = fastapi.APIRouter()

class FlowerData(BaseModel):
    sepal_length: float = Field(...)
    sepal_width: float = Field(...)
    petal_length: float = Field(...)
    petal_width: float = Field(...)


@router.post('/')
async def classify_flower(payload: FlowerData):
    predictor = IrisPredictorV1()
    flower_data_dict = dict(payload)
    flower_data = [flower_data_dict[key] for key in flower_data_dict.keys()]
    prediction = predictor.predict(flower_data)
    return prediction

