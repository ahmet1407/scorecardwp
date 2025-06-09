def detect_platform(url):
    url = url.lower()
    if "amazon" in url:
        return "amazon"
    elif "hepsiburada" in url:
        return "hepsiburada"
    elif "trendyol" in url:
        return "trendyol"
    else:
        raise Exception("Platform algılanamadı.")
