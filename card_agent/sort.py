from card_agent.constant import CATEGORY_MAPPING

def recommend_cards_by_usage(cards_to_sort, primary_category):
    """
    Scores and sorts a list of cards based on the rewards for a specific category.

    Args:
        cards_to_sort (list): A list of card objects (already filtered for eligibility).
        primary_category (str): The user's primary spending category (e.g., 'dining').

    Returns:
        list: A list of cards sorted by their reward value for that category, descending.
    """
   
    reward_keys = CATEGORY_MAPPING.get(primary_category.lower())
    if not reward_keys:
        print(f"Warning: Category '{primary_category}' is not recognized. Cannot sort by usage.")
        return cards_to_sort 

    scored_cards = []
    for card in cards_to_sort:
        rewards = card.get('rewards_details', {})
        max_reward_for_category = 0
        
      
        for key in reward_keys:
            if key in rewards:
                max_reward_for_category = max(max_reward_for_category, rewards[key])
        
        if max_reward_for_category > 0:
            scored_cards.append({
                "card": card,
                "reward_value": max_reward_for_category
            })


    sorted_by_reward = sorted(scored_cards, key=lambda x: x['reward_value'], reverse=True)
    

    return [item['card'] for item in sorted_by_reward]