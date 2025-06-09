import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        name = soup.select_one("#productTitle")
        price = soup.select_one(".a-price .a-offscreen")

        return {
            "name": name.get_text(strip=True) if name else "Ürün adı bulunamadı",
            "price": price.get_text(strip=True) if price else "Fiyat bulunamadı",
            "source": "amazon",
            "url": url
        }

    except Exception as e:
        raise Exception("Amazon sayfasına ulaşılamadı.") from e
