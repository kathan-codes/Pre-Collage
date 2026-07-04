import requests

def crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,Ethereum,Solana"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url,headers=headers,timeout=5)
        if response.status_code == 200:
            data = response.json()
            BTC_price = data["bitcoin"]["usd"]
            ETH_price = data["ethereum"]["usd"]
            SOL_price = data["solana"]["usd"]
            print("====================================")
            print("💰 LIVE CRYPTO PRICES 💰")
            print("====================================")
            print(f"Bitcoin (BTC):  ${BTC_price:,} USD")
            print(f"Ethereum (ETH):  ${ETH_price:,} USD")
            print(f"Solana (SOL): ${SOL_price:,} USD")
            print("====================================")
        else:
            print(f"Failed to get data. Error code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

crypto_price()