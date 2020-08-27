DISCOUNT = 0.9
item_list = []
number_of_items = int(input("Number of items:"))
for i in range(number_of_items):
    item_list.append(float(input("Price of item:")))
cost_sum = sum(item_list)
total_cost = 0
if cost_sum >= 100:
    total_cost = cost_sum * DISCOUNT
else:
    total_cost = cost_sum
print("Total price for", number_of_items, "items is $", round(total_cost, 2))
