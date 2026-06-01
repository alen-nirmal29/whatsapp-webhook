from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

client.messages.create(
    body="Hello from my AI outreach system from ganit",
    from_="whatsapp:+14155238886",
    to="whatsapp:+918056498879"
)

print("Message sent")