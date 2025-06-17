from smartapi import SmartConnect
import pyotp
import os

# === Login Details ===
API_KEY = os.getenv("ANGEL_API_KEY")
CLIENT_ID = os.getenv("ANGEL_CLIENT_ID")
TOTP_SECRET = os.getenv("ANGEL_TOTP_SECRET")

# === Login Function ===
obj = SmartConnect(api_key=API_KEY)
totp = pyotp.TOTP(TOTP_SECRET).now()

try:
    session_data = obj.generateSession(CLIENT_ID, totp)
    access_token = session_data['data']['access_token']
    
    # Save to file or database
    with open("access_token.txt", "w") as f:
        f.write(access_token)
    
    print("✅ ACCESS_TOKEN updated:", access_token)

except Exception as e:
    print("❌ Login error:", e)
