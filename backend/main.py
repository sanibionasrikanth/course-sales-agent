from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# Create FastAPI app
app = FastAPI()

# Enable CORS (Important for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class Customer(BaseModel):
    customerName: str
    phone: str
    courseName: str
    language: str


# Test route
@app.get("/")
def home():
    return {"message": "FastAPI Backend Running Successfully 🚀"}


# Form submit route
@app.post("/submit")
def submit_form(data: Customer):
    print("data",data)
    # n8n webhook URL
    n8n_webhook_url = "https://hypochloremic-carlita-allopatrically.ngrok-free.dev/webhook-test/sales-call"

    payload = {
        "customerName": data.customerName,
        "phone": data.phone,
        "courseName": data.courseName,
        "language": data.language
    }

    try:
        response = requests.post(n8n_webhook_url, json=payload)

        return {
            "status": "success",
            "message": "Data sent to n8n successfully",
            "n8n_response": response.text
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }