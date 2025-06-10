from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# === CONFIGURE THESE ===
CLIENT_ID = "YOUR_CLIENT_ID"
API_KEY = "YOUR_API_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Get from Angel SmartAPI
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

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received:", data)

    signal = data.get("signal")  # Example: "BUY" or "SELL"
    symbol = data.get("symbol", "RELIANCE-EQ")
    qty = int(data.get("qty", 1))

    if signal == "BUY":
        side = "BUY"
    elif signal == "SELL":
        side = "SELL"
    else:
        return jsonify({"status": "ignored"})

    order_data = {
        "variety": "NORMAL",
        "tradingsymbol": symbol,
        "symboltoken": "",  # Optional: if known
        "transactiontype": side,
        "exchange": "NSE",
        "ordertype": "MARKET",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "0",
        "quantity": qty
    }

    res = requests.post(f"{BASE_URL}/rest/secure/angelbroking/order/v1/placeOrder",
                        headers=HEADERS, json=order_data)
    print("Angel Response:", res.json())

    return jsonify({"status": "order sent", "angel_response": res.json()}), 200

@app.route('/')
def home():
    return "Angel One Webhook is live!"

if __name__ == '__main__':
    app.run(debug=True)
