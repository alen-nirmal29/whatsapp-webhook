from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):

    form_data = await request.form()

    print("Message:", form_data.get("Body"))
    print("Sender:", form_data.get("From"))

    return "OK"