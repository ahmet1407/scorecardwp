from utils.scrape_amazon import scrape_amazon_product
from utils.scrape_hepsiburada import scrape_hepsiburada_product
from utils.scrape_trendyol import scrape_trendyol_product

def get_scraper_for_url(platform):
    if platform == "amazon":
        return scrape_amazon_product
    elif platform == "hepsiburada":
        return scrape_hepsiburada_product
    elif platform == "trendyol":
        return scrape_trendyol_product
    else:
        return None
