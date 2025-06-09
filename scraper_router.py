from utils.detect_platform import detect_platform
from utils.scrape_amazon import scrape_amazon_product
from utils.scrape_hepsiburada import scrape_hepsiburada_product
from utils.scrape_trendyol import scrape_trendyol_product

def scrape_link(link_or_query: str) -> dict:
    platform = detect_platform(link_or_query)
    print(f"🧭 Platform tespiti: {platform}")

    if platform == "amazon":
        return scrape_amazon_product(link_or_query)
    elif platform == "hepsiburada":
        return scrape_hepsiburada_product(link_or_query)
    elif platform == "trendyol":
        return scrape_trendyol_product(link_or_query)
    else:
        raise ValueError("Desteklenmeyen platform veya geçersiz link.")
