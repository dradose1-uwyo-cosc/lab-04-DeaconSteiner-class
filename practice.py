items = ["Milk", "Eggs", "Coffee", "Batteries", "Chicken"]
prices = [2.99, 4.50, 6.99, 7.99, 11.00]

for index in range(len(items)):
    print(f'I bought {items[index]} for ${prices[index]}')


sum = 0
for i in prices:
    sum += i
    
print(f"I paid ${sum} for everything!")


PriceToRemove = index(max(prices))

del prices[PriceToRemove]
del items[PriceToRemove]