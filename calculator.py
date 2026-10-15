# Resale Profit Calculator

item_name = "PlayStation 5"
purchase_price = 250.00
selling_price = 390.00
shipping_cost = 20.00
selling_fees = 45.00

total_cost = purchase_price + shipping_cost + selling_fees
profit = selling_price - total_cost

print("Resale Profit Calculator")
print("------------------------")
print("Item: " + item_name)
print("Purchase price: $" + str(purchase_price))
print("Selling price: $" + str(selling_price))
print("Total expenses: $" + str(total_cost))
print("Estimated profit: $" + str(profit))

if profit > 0:
    print("This item could be profitable!")
else:
    print("This item may not be worth reselling.")

