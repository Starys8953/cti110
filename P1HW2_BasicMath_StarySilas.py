#A simple math format for calculating a tax
#06/12/2022
#CTI-110 P1HW2- Basic Math
#Silas Stary
user_expense = input('Enter name of expense:')
user_charge = int(input('Enter monthly charge:'))
print('Bill:',user_expense,'--------- Before Tax:',user_charge)
print('Monthly Tax:', user_charge * (6 / 100))
print('Monthly Charge:', user_charge * (6 /100) + user_charge)
print('Annual Charge:', (user_charge * (6 /100) + user_charge) * 12)
