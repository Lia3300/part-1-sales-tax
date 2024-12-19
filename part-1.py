SALES_TAX_RATE = 0.06625
COST = 0

cost = float(input("Enter the cost of the item:"))

sales_tax = cost * SALES_TAX_RATE

total_cost = cost + sales_tax

print(total_cost)
