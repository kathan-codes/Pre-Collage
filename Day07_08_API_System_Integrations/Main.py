import os
from dotenv import load_dotenv
import requests
headers = {
    "User-Agent": "mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
load_dotenv()
file = os.getenv("ENV_FILE")
url = os.getenv("WEATHER_API_URL")
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()
data = response.json()
temp = data['current']['temperature_2m']
humidity = data['current']['relative_humidity_2m']
code = data['current']['weather_code']

if code == 0:
    weather = "Clear Sky ☀️"
    print(weather)
elif code in [1, 2, 3]:
    weather = "Partly Cloudy ☁️"
    print(weather)
else:
    weather = "Unsettled Weather 🌧️"
    print(weather)

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

message = (
    f"📊 *DAILY WEATHER UPDATE* 📊\n\n"
    f"🌤️ *Condition:* {weather}\n"
    f"🌡️ *Temperature:* {temp}°C\n"
    f"💧 *Humidity :* {humidity}%"
)

telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown" # Allows Telegram to style bold text/emojis properly
}

# 4. Fire the POST request
tg_response = requests.post(telegram_url, json=payload, timeout=10)

if tg_response.status_code == 200:
    print("🚀 Weather report delivered directly to Telegram!")
else:
    print(f"❌ Failed to send to Telegram: {tg_response.status_code} - {tg_response.text}")