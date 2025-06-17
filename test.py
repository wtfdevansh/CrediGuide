from card_agent.recommender import Recommender

Recommender = Recommender()

result  = Recommender.recommend(700, 50000, 100, "travel")

print(result)