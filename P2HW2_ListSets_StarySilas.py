#Basic List and Sets
#06/19/2022
#CTI-110 P2HW2 - Lists and Sets
#Silas Stary
num_1 = int(input('Enter num 1:'))
num_2 = int(input('Enter num 2:'))
num_3 = int(input('Enter num 3:'))
num_4 = int(input('Enter num 4:'))
num_5 = int(input('Enter num 5:'))
num_6 = int(input('Enter num 6:'))

user_numbers = [num_1, num_2, num_3, num_4, num_5, num_6]
print('Created list')
print(user_numbers)
print('Smallest number in list:', min(user_numbers))
print('Largest number in list:', max(user_numbers))
print('Sum of numbers in list:', sum(user_numbers))
print('Average of numbers in list:', sum(user_numbers)/len(user_numbers))
set_1 = set([num_1, num_2, num_3, num_4, num_5, num_6])
print('Created set')
print(set_1)

