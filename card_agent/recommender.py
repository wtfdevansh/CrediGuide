from card_agent.data_loader import load_card_data
from card_agent.tier_logic import get_tier
from card_agent.sort import recommend_cards_by_usage

data = load_card_data()
card_data = data.load_data()


class Recommender:

    def __init__(self , card_data = card_data):
        self.card_data = card_data


    def sort_by_usage(self, cards, primary_usage):
        """
        Sorts the list of cards based on the primary usage category.
        
        Args:
            cards (list): A list of card dictionaries.
            primary_usage (str): The primary usage category to sort by.
        
        Returns:
            list: A sorted list of cards based on the primary usage category.
        """
        
        return recommend_cards_by_usage(cards, primary_usage)


    
    def recommend(self , credit_score , income , fee , usage):
        """
        Recommend a card based on credit score, income, fee, and usage.
        
        Args:
            credit_score (int): The user's credit score.
            income (float): The user's annual income.
            fee (float): The maximum annual fee the user is willing to pay.
            usage (str): The primary usage of the card (e.g., "travel", "cashback", "rewards").
        
        Returns:
            list: A list of recommended cards.
        """

        tier = get_tier(income)
        
        recommendations = []

        for card in self.card_data:

            elegibility = card.get('eligibility')
            annual_fee = card.get('annual_fee')

            if elegibility['credit_score'] <= credit_score and \
                annual_fee <= fee and \
                elegibility['income_level'] == tier:  
            
                recommendations.append(card)

        # Sort the recommendations based on the primary usage category

        sorted_recommendations = self.sort_by_usage(recommendations, usage)
        
        return recommendations
    

