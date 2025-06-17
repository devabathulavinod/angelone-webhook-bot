from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        print("✅ Received:", data)
        return jsonify({"status": "success"}), 200
    else:
        print("❌ Unsupported content type")
        return "Unsupported Media Type", 415

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




