from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1370781642184065115/SyXEh-OWDqprhBnKswydmfTYyypY_u7dvJ9aqU6oZb32jAynjZL_b0ZzcsoZ9L3DYcR4"

@app.route("/", methods=["POST"])
def receive_webhook():
    data = request.json

    customer_email = data.get("email", "Unknown")
    currency = data.get("currency", "USD")
    price_cents = data.get("price", 0)
    price = f"{int(price_cents) / 100:.2f} {currency}"
    product_name = data.get("items", [{}])[0].get("product_name", "Unknown Product")
    date_unix = data.get("date", 0)
    date_str = datetime.datetime.utcfromtimestamp(date_unix).strftime('%Y-%m-%d %H:%M:%S UTC')

    embed = {
        "title": "🛒 New Purchase!",
        "description": f"Someone just bought **{product_name}**!",
        "color": 5814783,
        "fields": [
            {"name": "💻 Product", "value": product_name, "inline": True},
            {"name": "💰 Price", "value": price, "inline": True},
            {"name": "📧 Buyer", "value": customer_email, "inline": False},
            {"name": "🕒 Time", "value": date_str, "inline": False}
        ]
    }

    requests.post(DISCORD_WEBHOOK_URL, json={"embeds": [embed]})

    return "Webhook received", 200
