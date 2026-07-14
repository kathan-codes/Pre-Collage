# Days 7 & 8: API System Integrations ☁️🤖

## 📌 Project Overview
A smart weather notification system that fetches location-based weather forecasts from a free API and sends a automated alert message to a communication platform (like Discord or Telegram) if rain is predicted for the day.

## 🎯 Learning Objectives
* Understand how to sequentially link multiple external API systems together.
* Learn to secure sensitive credentials (API keys, tokens, webhooks) using environment files.
* Master outbound webhook structures and JSON payloads.

## 🛠️ Core Libraries Used
* `requests` - For calling the weather API and sending webhook payloads.
* `   ` - For securely loading credentials from a hidden `.env` file.

## 🚀 How To Run
1. Navigate to this directory.
2. Create a `.env` file in this directory and add your private credentials:
   ```env
   DISCORD_WEBHOOK_URL=your_webhook_url_here