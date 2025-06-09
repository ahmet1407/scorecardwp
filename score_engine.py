from score_utils import (
    calculate_satisfaction,
    calculate_flaw_score,
    calculate_aura_score,
    calculate_expert_score,
)

def generate_scorecard(product):
    return {
        "name": product["name"],
        "price": product["price"],
        "source": product["source"],
        "url": product["url"],
        "scores": {
            "satisfaction": calculate_satisfaction(product),
            "flaw": calculate_flaw_score(product),
            "aura": calculate_aura_score(product),
            "expert": calculate_expert_score(product),
        }
    }
