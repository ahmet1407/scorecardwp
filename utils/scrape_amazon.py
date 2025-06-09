import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise Exception("Amazon sayfasına ulaşılamadı.")

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.select_one("#productTitle")
    price = soup.select_one(".a-price .a-offscreen")

    if not title or not price:
        raise Exception("Amazon ürünü bulunamadı.")

    return {
        "name": title.get_text(strip=True),
        "price": price.get_text(strip=True),
        "platform": "Amazon"
    }
