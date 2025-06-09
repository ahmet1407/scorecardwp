import requests
from bs4 import BeautifulSoup

def scrape_trendyol_product(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "tr-TR,tr;q=0.9"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise ValueError("Trendyol sayfasına ulaşılamadı.")

    soup = BeautifulSoup(response.text, "html.parser")

    # Ürün adı
    name_tag = soup.find("h1", class_="pr-new-br")
    name = name_tag.get_text(strip=True) if name_tag else None

    # Fiyat
    price_tag = soup.select_one("span.prc-dsc")
    price = price_tag.get_text(strip=True).replace("\u202f", "") if price_tag else None

    # Yorumlar
    review_tags = soup.select("p.comment-text")
    reviews = [tag.get_text(strip=True) for tag in review_tags[:5]] if review_tags else []

    if not name or not price:
        raise ValueError("Ürün adı veya fiyatı alınamadı. Sayfa yapısı değişmiş olabilir.")

    return {
        "name": name,
        "price": price,
        "reviews": reviews
    }
