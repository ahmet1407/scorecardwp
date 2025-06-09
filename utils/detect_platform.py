def detect_platform(link_or_query):
    link = link_or_query.lower()
    if "amazon" in link:
        return "amazon"
    elif "hepsiburada" in link:
        return "hepsiburada"
    elif "trendyol" in link:
        return "trendyol"
    else:
        return None
