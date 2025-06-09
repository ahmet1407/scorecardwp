import requests
from bs4 import BeautifulSoup

def scrape_trendyol_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise Exception("Trendyol sayfasına erişilemedi.")

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        name = soup.find("h1", class_="pr-new-br").get_text(strip=True)
    except:
        name = soup.find("h1", class_="product-name").get_text(strip=True)

    try:
        price = soup.find("span", class_="prc-dsc").get_text(strip=True)
    except:
        price = soup.find("span", class_="prc-org").get_text(strip=True)

    image_tag = soup.find("img", {"class": "product-image"})
    image_url = image_tag['src'] if image_tag else ""

    return {
        "name": name,
        "price": price,
        "image": image_url,
        "source": "trendyol"
    }
