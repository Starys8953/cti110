# CTI-110
# P4HW2 - Expenses
# Silas Stary 
# 07/3/2022

#start by asking user to input original balance
account_balance =int(input('Enter starting amount in account $'))

#set up variables to run the loop while asking user to input expenses
x = 1
user_char = 'y'
user_expenses = []
while user_char == 'y':
    expense_x = int(input('Enter expense ' + str(x) +':'))
    user_char =input('Do you want to enter another expense?(y/n)')
    x = x + 1
    user_expenses.append(expense_x)
#display the account balance before and after expenses are calculated
print('Amount in account before expenses subtracted $',account_balance)
print('Number of expenses entered:', len(user_expenses))
print('Amount in account After expenses subtracted is $', account_balance - sum(user_expenses))
    
