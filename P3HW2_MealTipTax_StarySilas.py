# CTI-110
# P3HW2 - MealTipTax
# Silas Stary
# 06/19/2022
# Calculating the cost of a meal tip tax
meal_cost = int(input('Please enter cost of meal:'))
#input food cost
tip_percentage = float(input('Enter tip amount of 15, 18, or 20:'))#input tip percentage
if tip_percentage == 0.15:
    tax_percentage = float(0.06)
    print('Meal price:', meal_cost)
    print('Tax:', tax_percentage)
    print('Tip:', tip_percentage) #prints meal cost and both percentages
    print('Total:',(meal_cost * tip_percentage) + (meal_cost * tax_percentage) + meal_cost)
elif tip_percentage == 0.18:
    tax_percentage = float(0.06)
    print('Meal price:', meal_cost)
    print('Tax:', tax_percentage)
    print('Tip:', tip_percentage) #prints meal cost and both percentages
    print('Total:',(meal_cost * tip_percentage) + (meal_cost * tax_percentage) + meal_cost)
elif tip_percentage == 0.20:
    tax_percentage = float(0.06)
    print('Meal price:', meal_cost)
    print('Tax:', tax_percentage)
    print('Tip:', tip_percentage) #prints meal cost and both percentages
    print('Total:',(meal_cost * tip_percentage) + (meal_cost * tax_percentage) + meal_cost)    
#displays the total cost
else:
    print('Error: please enter above listed numbers.')
