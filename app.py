from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# Allow frontend from localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8080"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
model = joblib.load("titanic_model.pkl")

# Define request model
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Cabin: int
    Embarked: int

@app.post("/predict")
def predict(passenger: Passenger):
    data = [[
        passenger.Pclass,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Fare,
        passenger.Cabin,
        passenger.Embarked
    ]]
    prediction = model.predict(data)[0]
    return {"Survived": int(prediction)}
