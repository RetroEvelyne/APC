def breakeven(cost_per_item: float, revenue_per_item: float, fixed_costs: float) -> float:
    return fixed_costs / (revenue_per_item - cost_per_item)


cost_per_item = 20.0
revenue_per_item = 40.0
fixed_costs = 50000.0

print(f"Cost for each item: £{cost_per_item}")
print(f"Sale price for each item: £{revenue_per_item}")
print(f"Fixed costs: £{fixed_costs}")
print(f"Profit per item: £{revenue_per_item - cost_per_item}")

print(f"Breakeven: {breakeven(cost_per_item, revenue_per_item, fixed_costs)} items")