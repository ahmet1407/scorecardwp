import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise ValueError("Amazon sayfasına ulaşılamadı.")

    soup = BeautifulSoup(response.text, "html.parser")

    # Ürün adı
    name_tag = soup.select_one("#productTitle")
    name = name_tag.get_text(strip=True) if name_tag else None

    # Fiyat (birden fazla varyasyon var; en sağlam yol span.a-price > span.a-offscreen)
    price_tag = soup.select_one('span.a-price > span.a-offscreen')
    price = price_tag.get_text(strip=True) if price_tag else None

    # Yorumlar
    review_tags = soup.select("span[data-hook='review-body']")
    reviews = [tag.get_text(strip=True) for tag in review_tags[:5]] if review_tags else []

    # Hata kontrolü
    if not name or not price:
        raise ValueError("Ürün adı veya fiyatı alınamadı. Sayfa yapısı değişmiş olabilir.")

    return {
        "name": name,
        "price": price,
        "reviews": reviews
    }
