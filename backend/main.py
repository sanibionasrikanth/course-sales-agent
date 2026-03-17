
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# CORS (OK for now, restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Customer(BaseModel):
    customerName: str
    phone: str
    courseName: str
    language: str


@app.get("/")
def home():
    return {"message": "FastAPI Backend Running Successfully 🚀"}


@app.post("/submit")
def submit_form(data: Customer):
    print("Received data:", data)

    # ✅ Production n8n webhook URL
    n8n_webhook_url = "https://n8n-1-xw0r.onrender.com/webhook/sales-call"

    payload = {
        "customerName": data.customerName,
        "phone": data.phone,
        "courseName": data.courseName,
        "language": data.language
    }

    try:
        # ✅ Add timeout (important)
        response = requests.post(
            n8n_webhook_url,
            json=payload,
            timeout=10
        )

        print("n8n status:", response.status_code)
        print("n8n response:", response.text)

        return {
            "status": "success",
            "n8n_status": response.status_code,
            "n8n_response": response.text
        }

    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

        return {
            "status": "error",
            "message": str(e)
        }