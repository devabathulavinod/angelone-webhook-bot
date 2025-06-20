from flask import Flask, request, jsonify
import pyotp
import requests
import time

app = Flask(__name__)

# === CONFIGURE THESE ===
TOTP_SECRET = "RSC37LE3FNM3W45NNDBVP4W134"
CLIENT_ID = "D224687"
API_KEY = "XUdpW7oz"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BASE_URL = "https://apiconnect.angelbroking.com"

HEADERS = {
    "X-PrivateKey": API_KEY,
    "X-SourceID": "WEB",
    "X-ClientLocalIP": "127.0.0.1",
    "X-ClientPublicIP": "127.0.0.1",
    "X-MACAddress": "00:00:00:00:00:00",
    "X-UserType": "USER",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def generate_otp():
    totp = pyotp.TOTP(TOTP_SECRET)
    return totp.now()

import json
# … other imports above …

@app.route("/webhook", methods=["POST"])
def on_webhook():
    import json

    # ── Force-parse raw body as JSON ──
    raw = request.data
    try:
        data = json.loads(raw)
    except Exception:
        data = request.get_json(force=True)

    print("🔔 Received alert:", data)

    # ── Now your regular logic ──
    signal = data.get("signal")
    symbol = data.get("symbol")
    qty    = data.get("qty", "1")

    order_payload = {
        "variety":        "NORMAL",
        "tradingsymbol":  symbol,
        "symboltoken":    "99926009",
        "transactiontype": signal,
        "exchange":       "NSE",
        "ordertype":      "MARKET",
        "producttype":    "INTRADAY",
        "duration":       "DAY",
        "price":          "0",
        "squareoff":      "0",
        "stoploss":       "0",
        "quantity":       qty
    }

    client = get_client()
    resp   = client.placeOrder(order_payload)
    print("📤 Order response:", resp)
    return jsonify(resp), 200
