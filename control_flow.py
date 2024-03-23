def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = discount_percent / 100 * price
        new_price = price - discount
        print("Discounted price: ", new_price)
        return new_price
    else:
        print("No dicount applied!!")
        return price
        


print("Enter original price:")
price = float(input())
print("Enter discount percentage: ")
discount_percent = float(input())

calculate_discount(price, discount_percent)
