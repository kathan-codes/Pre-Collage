import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://timesofindia.indiatimes.com/"

with open("Pre-Collage\Day02_News_Headline_Aggregator\Headlines.txt","w",) as f:
    f.write("==================================================================\n")
    f.write("               Todays Headlines Form Times Of India               \n")
    f.write("==================================================================\n")

def get_headlines():
    response = requests.get(url,headers=headers,timeout=5)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,'html.parser')
    headlines = soup.find_all('div',class_="Kt6Pm style_change T5Q6J")

    
    with open("Pre-Collage/Day02_News_Headline_Aggregator/Headlines.txt","a",encoding="utf-8") as f:
        for index, h in enumerate(headlines, start=1):
            print(f"{index}. {h.get_text(strip=True)}\n")   
            f.write(f"{index}. {h.get_text(strip=True)}\n")
    
    print(f"\n✅ Successfully saved {len(headlines)} headlines to Pre-Collage/Day02_News_Headline_Aggregator/Headline.txt")

get_headlines()