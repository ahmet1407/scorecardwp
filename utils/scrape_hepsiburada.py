import requests
from bs4 import BeautifulSoup

def scrape_hepsiburada_product(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise Exception("Hepsiburada sayfasına ulaşılamadı.")

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.select_one("h1")
    price = soup.select_one(".price")

    if not title or not price:
        raise Exception("Hepsiburada ürünü bulunamadı.")

    return {
        "name": title.get_text(strip=True),
        "price": price.get_text(strip=True),
        "platform": "Hepsiburada"
    }
