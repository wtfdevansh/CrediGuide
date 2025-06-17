def get__tier(annual_income):
    """Converts a user's annual income into a defined tier."""
    if annual_income < 35000:
        return "linient"
    elif annual_income < 75000:
        return "stable"
    elif annual_income < 120000:
        return "premium"
    else:
        return "business"



