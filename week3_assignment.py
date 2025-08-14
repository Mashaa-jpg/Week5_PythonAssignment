def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price given the original price and discount percentage.

    Parameters:
    original_price (float): The original price of the item.
    discount_percentage (float): The discount percentage to apply.

    Returns:
    float: The price after applying the discount.
    """
    if original_price < 0 or discount_percentage < 0:
        raise ValueError("Original price and discount percentage must be non-negative.")
    
    if discount_percentage >= 20:
     discount_amount = (discount_percentage / 100) * original_price
     return original_price - discount_amount
    else:
     return original_price
    # 👇 User input and output section
try:
    original = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    final_price = calculate_discounted_price(original, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")
