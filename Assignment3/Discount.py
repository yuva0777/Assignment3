price = float(input("Enter the price of the item: "))
if price > 1000:
    price -= price * 0.10  
elif price > 500:
    price -= price * 0.05  
print(f"The final price is: {price}")
