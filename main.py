from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from twilio.rest import Client
import os

app = FastAPI()

MESSAGES = []


class WhatsAppRequest(BaseModel):
    phone: str
    message: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/send-whatsapp")
async def send_whatsapp(req: WhatsAppRequest):
    try:
        client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )

        message = client.messages.create(
            body=req.message,
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{req.phone}"
        )

        return {"success": True, "message_sid": message.sid}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()

    message = {
        "from": form_data.get("From"),
        "body": form_data.get("Body")
    }

    MESSAGES.append(message)

    print("Stored:", message)

    return "OK"


@app.get("/pending-messages")
def pending_messages():
    return MESSAGES