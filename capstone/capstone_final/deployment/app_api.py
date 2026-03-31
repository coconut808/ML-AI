from fastapi import FastAPI
import joblib
from pydantic import BaseModel

model = joblib.load("final_model.pkl")

WIKI_BASE_URL = "http://localhost:8501"

class TicketSubject(BaseModel):
	subject: str

app = FastAPI()

@app.get("/")
def root():
    print("Hello")
    return {"message": "Ticket Classifier API"}

@app.post("/predict")
def predict_ticket_type(ticket: TicketSubject):
    prediction = model.predict([ticket.subject])
    return {"subject": ticket.subject, 
            "predicted_type": prediction[0], 
            "message": (
                f"Thanks for submitting your ticket! "
                f"In the interim, please visit the documentation page {WIKI_BASE_URL}/{prediction[0]}.html "
                f"or check the FAQ page here {WIKI_BASE_URL}/")
            }