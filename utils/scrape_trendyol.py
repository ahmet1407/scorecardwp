import requests
from bs4 import BeautifulSoup

def scrape_trendyol_product(url):
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

        name = soup.select_one("h1.pr-new-br")
        price = soup.select_one("span.prc-dsc")

        return {
            "name": name.get_text(strip=True) if name else "Ürün adı bulunamadı",
            "price": price.get_text(strip=True) if price else "Fiyat bulunamadı",
            "source": "trendyol",
            "url": url
        }

    except Exception as e:
        raise Exception("Trendyol sayfasına ulaşılamadı.") from e
