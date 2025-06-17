# auto_login.py
import time
import pyotp
import requests
from smartapi import SmartConnect

# === CREDENTIALS ===
CLIENT_ID = "YOUR_CLIENT_ID"
PIN = "YOUR_PIN"
TOTP_SECRET = "YOUR_TOTP_SECRET"
API_KEY = "YOUR_API_KEY"  # Optional if used in older SDK

# === SETUP SMARTCONNECT ===
obj = SmartConnect(api_key=CLIENT_ID)

# === GENERATE TOTP ===
totp = pyotp.TOTP(TOTP_SECRET).now()

# === LOGIN ===
data = obj.generateSession(CLIENT_ID, PIN, totp)

if "data" in data:
    access_token = data['data']['access_token']
    print("✅ Access Token:", access_token)

    # Save token to file
    with open("access_token.txt", "w") as f:
        f.write(access_token)
else:
    print("❌ Login failed:", data)
