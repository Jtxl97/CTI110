#CTI-110
#P3HW2 - BasicMath
#Jonathan Lopresto
#3/18/2020

#Prompt user to imput two numbers
#Calculations
#Prompt user to select an option from a menu including Add Numbers, Multiply Numbers, Subtract Numbers, Exit
#When Add Numbers is selected display the sum of the two numbers
#When Multiply Numbers is selected display the product of the two numbers
#When Subtract Numbers is selected display the difference of the two numbers
#When Exit is selected display a message that the program will terminate
#When none of the above options are selected display an error message

num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))
num_sum = num_1 + num_2
num_product = num_1 * num_2
num_difference = num_1 - num_2
print(' -----------MENU-----------')
print('1) Add Numbers')
print('2) Multiply Numbers')
print('3) Subtract Numbers')
print('4) Exit')
print('---------------------------')
menu_choice = input('Choose from the menu above by entering a number 1-4: ')
if menu_choice == "1":
    print(num_sum)
elif menu_choice == "2":
    print(num_product)
elif menu_choice == "3":
    print(num_difference)
elif menu_choice == "4":
    print('The program will terminate')
else:
    print('Error: Invaild menu choice entered')
