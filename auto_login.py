import os
from smartapi.smartConnect import SmartConnect

API_KEY = os.environ["API_KEY"]
CLIENT_CODE = os.environ["CLIENT_CODE"]
PASSWORD = os.environ["PASSWORD"]

obj = SmartConnect(api_key=API_KEY, client_code=CLIENT_CODE, password=PASSWORD)

data = obj.generateSession(CLIENT_CODE, PASSWORD)
print("✅ Login successful:", data)
