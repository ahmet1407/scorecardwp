from utils.detect_platform import detect_platform
from scraper_manager import get_scraper_for_url

def scrape_link(link_or_query):
    platform = detect_platform(link_or_query)
    scraper = get_scraper_for_url(platform)
    return scraper(link_or_query)
