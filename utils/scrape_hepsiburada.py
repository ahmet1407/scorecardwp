import requests
from bs4 import BeautifulSoup

def scrape_hepsiburada_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise ValueError("Hepsiburada sayfasına ulaşılamadı.")

    soup = BeautifulSoup(response.text, "html.parser")

    # Ürün adı
    name_tag = soup.select_one('h1[data-test-id="product-title"]')
    name = name_tag.text.strip() if name_tag else None

    # Fiyat
    price_tag = soup.select_one('div[data-test-id="price-container"] > div > span')
    price = price_tag.text.strip() if price_tag else None

    # Yorumlar üzerinden skor üretimi için örnek birkaç yorum
    review_tags = soup.select('div[class*="review-text"]')
    reviews = [tag.get_text(strip=True) for tag in review_tags[:5]] if review_tags else []

    # Hata fırlat, eğer temel veriler yoksa
    if not name or not price:
        raise ValueError("Ürün adı veya fiyatı alınamadı. Sayfa yapısı değişmiş olabilir.")

    return {
        "name": name,
        "price": price,
        "reviews": reviews
    }
