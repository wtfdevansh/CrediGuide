from card_agent.recommender import Recommender

Recommender = Recommender()

result  = Recommender.get_credit_card_recommendation(700, 50000, 100, "travel")

print(result)