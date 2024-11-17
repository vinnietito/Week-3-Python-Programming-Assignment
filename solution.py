def calculate_discount(price, discount_percent):
    
    """
    Calculate the final price after applying a discount.
    
    Args:
        Price(float): The original price of the item
        discount_percent(float): The discount percentage.
        
    Returns:
        float: The final price after applying the discount,
        or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price
    
    
    # Prompts user for inputs
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("ENter the discount percentage: "))
        