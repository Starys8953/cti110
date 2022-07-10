# making a rng math quiz
# 7/10/2022
# CTI-110 P5HW2 - Math Quiz
# Silas Stary

#first import the rng
import random

rng_1 = random.randint(1,1000)
rng_2 = random.randint(1,1000)
#then i set up the functions for the menu
print('Welcome to Math Quiz')
def menu_screen():
    print('MAIN MENU')
    print('-' * 20)

def main_menu():
    menu_list = ["1. Adding Random Numbers","2. Subtracting Random Numbers","3. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
#now i set up the inputs to select within the menu    
def get_user_input():
    user_input = int(input('Please choose one of the menu options:'))
    while user_input < 4 or user_input >=0:
        return user_input
    else:
        print("Invalid menu option.")
        user_input = int(input("Please try again:"))

#here is the (long) function for the quiz itself
def menu_option():
    if get_user_input() == 1:
        print(rng_1)
        print('+',rng_2)
        answer = int(input('Enter Answer:'))

        counter = 0
        while answer != (rng_1 + rng_2):
            if answer < (rng_1 + rng_2):
                counter = counter + 1
                print('Sorry, guess is too low.')
                answer = int(input('try again:'))
                
            elif answer > (rng_1 + rng_2):
                counter = counter + 1
                print('Sorry, guess is too high.')
                answer = int(input('try again:'))
                
   
        else:
            print('Congratulations!!!! your answer is correct...')
            print('Number of guesses:', counter)
            return main()
    elif get_user_input() == 2:
        print(rng_1)
        print('-',rng_2)
        answer = int(input('Enter Answer:'))

        counter = 0
        while answer != (rng_1 - rng_2):
            if answer < (rng_1 - rng_2):
                counter = counter + 1
                print('Sorry, guess is too low.')
                answer = int(input('try again:'))
                
            elif answer > (rng_1 - rng_2):
                counter = counter + 1
                print('Sorry, guess is too high.')
                answer = int(input('try again:'))   
                
        else:
            print('Congratulations!!!! your answer is correct...')
            print('Number of guesses:', counter)
            return main()
    else:
        print('Thank you for playing...')
        print('Bye!!')

#this is how I set the whole thing up     
def main():
    menu_screen()
    main_menu()
    get_user_input()
    menu_option()
main()
#I do not know how I accidently got the input choise for the menu to repeat 3 times but I cannot figure out the fix


