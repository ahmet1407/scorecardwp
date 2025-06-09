def detect_platform(input_string: str) -> str:
    """
    Verilen link veya sorgudan platformu (amazon, hepsiburada, trendyol) tespit eder.
    """
    input_lower = input_string.lower()

    if "amazon.com.tr" in input_lower or "amazon." in input_lower:
        return "amazon"
    elif "hepsiburada.com" in input_lower:
        return "hepsiburada"
    elif "trendyol.com" in input_lower:
        return "trendyol"
    else:
        return "unknown"
