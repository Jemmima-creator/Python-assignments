# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Give discount only if 20% or more
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Get input from the user
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount)

# Print the result
if discount >= 20:
    print(f"The final price after {discount}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {original_price}")
    
