from card_agent.data_loader import load_card_data
from card_agent.tier_logic import get_tier
from card_agent.sort import recommend_cards_by_usage
from langchain.agents import tool
import json
from schema.schema import RecommendationResponse, RecommendedCard

from card_agent.tier_logic import TIER_HIERARCHY

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
    
    def find_suitable_cards(self, credit_score, income, fee):
        """
        Find suitable cards based on credit score, income, and annual fee.
        
        Args:
            credit_score (int): The user's credit score.
            income (float): The user's annual income.
            fee (float): The maximum annual fee the user is willing to pay.
        
        Returns:
            list: A list of suitable cards.
        """
        
        tier_index = TIER_HIERARCHY.index(get_tier(income))
        
        suitable_cards = []

        for card in self.card_data:

            elegibility = card.get('eligibility')
            annual_fee = card.get('annual_fee')

            if elegibility['credit_score'] <= credit_score and \
                annual_fee <= fee and \
                TIER_HIERARCHY.index(elegibility.get('income_level')) <= tier_index:  
            
                suitable_cards.append(card)

        return suitable_cards

    
    
    def get_credit_card_recommendations(self , credit_score:int , income:int , fee:int , usage: str)->str:
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

        suitable_cards = self.find_suitable_cards(credit_score, income, fee)

        if not suitable_cards:
            return "No suitable cards found based on your criteria."

        sorted_cards = self.sort_by_usage(suitable_cards, usage)

        if not sorted_cards:
            return "No cards found that match your primary usage category."

        recommended_card_models = []
        for card in sorted_cards[:3]:
            recommended_card_models.append(
                RecommendedCard(
                    card_name=card.get("name", "N/A"),
                    card_image=card.get("image_link", "N/A"),
                    issuer=card.get("issuer", "N/A"),
                    card_reward=card.get("rewards_summary", "N/A"),
                    card_benefits=card.get("benefits", []),
                    reason=f"Recommended for its benefits related to '{usage}' and a suitable fee structure.",
                    annual_fee=card.get("annual_fee", 0.0)
                )
            )

    
        summary_text = f"Based on your criteria, here are the top {len(recommended_card_models)} recommendations."
        final_response = RecommendationResponse(
            summary=summary_text,
            recommended_cards=recommended_card_models
        )

     
        return final_response.model_dump_json(indent=2)
    

