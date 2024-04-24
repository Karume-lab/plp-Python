def calculate_discount(price, discount_percentage):
    if discount_percentage >= 0.02:
        return price - (price * discount_percentage)
    return price

price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the original discount percentage: ")) / 100
final_price = calculate_discount(price, discount_percentage)
print(f"The final price is {final_price}")
