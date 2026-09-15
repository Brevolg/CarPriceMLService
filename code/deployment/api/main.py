from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

class Car(BaseModel):
    make_year: int
    engine_capacity: int
    km_driven: int


@app.get("/")
def home():
    return {"message": "Car price prediction"}

@app.post("/predict")
def predict(car: Car):
    data = pd.DataFrame(
        [
            {
                "make_year": car.make_year,
                "engine_capacity(CC)": car.engine_capacity,
                "km_driven": car.km_driven
            }
        ]
    )

    prediction = model.predict(data)

    return {"predicted_price": round(float(prediction[0]))}