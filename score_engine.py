from score_utils import calculate_scores

def generate_scorecard(product_data):
    scores = calculate_scores(product_data)
    return {
        "name": product_data.get("name"),
        "price": product_data.get("price"),
        "scores": scores
    }
