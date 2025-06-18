from pydantic import BaseModel, Field
from typing import List

class MyfunctionInput(BaseModel):
    credit_score: int = Field(description="credit score of the user")
    income: int = Field(description="user income needed to analyze the credit card")
    fee: int = Field(description="the fee user can give for credit card")
    usage:str = Field(description="whats the purpose of using credit card")

class RecommendedCard(BaseModel):
    """Data model for a single recommended credit card."""
    card_name: str = Field(description="The name of the credit card.")
    card_image: str = Field(description="A URL to an image of the credit card.")
    issuer: str = Field(description="The bank or company that issues the card.")
    card_reward: str = Field(description="The type of rewards offered by the card (e.g., cashback, points, miles).")
    card_benefits: List[str] = Field(description="A list of key benefits associated with the card, such as travel insurance, purchase protection, etc.")
    reason: str = Field(description="A brief explanation of why this card is recommended for the user.")
    annual_fee: float = Field(description="The annual fee of the card.")
    apply_link: str = Field(description="the url need to apply for card")

class RecommendationResponse(BaseModel):
    """Data model for the final list of recommendations."""
    summary: str = Field(description="A brief overall summary of the recommendation provided.")
    recommended_cards: List[RecommendedCard] = Field(description="A list of recommended credit cards.")
