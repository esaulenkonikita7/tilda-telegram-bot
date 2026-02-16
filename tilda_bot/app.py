from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    name = data.get("Name", "—")
    phone = data.get("Phone", "—")
    contact = data.get("Где_лучше_с_вами_связаться", "—")
    sphere = data.get("В_какой_сфере_работаете", "—")
    need = data.get("Выберите_что_сейчас_актуально_для_вашего_бизнеса", "—")
    budget = data.get("На_какой_ежемесячный_бюджет_ориентируетесь_для_привлечения_клиентов", "—")

    text = f"""🔥 Новый лид

👤 {name}
📞 {phone}
💬 {contact}

🏗 {sphere}
🎯 {need}
💰 {budget}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return "ok", 200


if __name__ == "__main__":
    app.run()
