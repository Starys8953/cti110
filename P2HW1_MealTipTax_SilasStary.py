# Calculating the cost of a meal tip tax
# 06/19/2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Stary
food_cost = int(input('Enter Food Cost:'))
tip_percentage = float(input('Enter Tip Percentage:'))
tax_percentage = float(input('Enter Tax Percentage:'))
print('Calculated Tip:', tip_percentage)
print('Calculated Tax:', tax_percentage)
print('Total cost including tip and tax:', (food_cost * tip_percentage) + (food_cost * tax_percentage) + food_cost)
