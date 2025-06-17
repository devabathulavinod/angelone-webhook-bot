# auto_login.py
import time
import pyotp
import requests
from smartapi import SmartConnect

# === CREDENTIALS ===
CLIENT_ID = "D224687"
PIN = "5678"
TOTP_SECRET = "RSC37LE3FNM3W45NNDBVP4W134"
API_KEY = "XUdpW7oz"  # Optional if used in older SDK

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
