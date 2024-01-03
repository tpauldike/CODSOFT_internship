#!/usr/bin/env python3
# A simple calculator that performs basic arithmetic operations

def execute(a, b, choice):
    '''perfoms the arithmetic operation based on the user's choice'''
    a = int(a)
    b = int(b)
    choice == choice.strip()

    if choice == '1':
        print(f'{a} + {b} = {a+b}')
    elif choice == '2':
        print(f'{a} - {b} = {a-b}')
    elif choice == '3':
        print(f'{a} × {b} = {a*b}')
    elif choice == '4':
        if (a % b) == 0:
            print(f'{a} ÷ {b} = {a//b}')
        else:
            print(f'{a} ÷ {b} = {a/b}')
    else:
        print(f'Error: "{choice}" is an invalid choice')


def is_valid(user_input):
    try:
        int(user_input.strip())
        return True
    except:
        print(f'"{user_input}" is not valid')
        return False


def valid_choice(choice):
    choice = choice.strip()
    options = [1, 2, 3, 4]

    for option in options:
        if option == int(choice):
            break
    return True



def quit(response):
    options = ['y', 'yes']
    if response.strip().lower() in options:
        return False
    else:
        return True


while True:
    print('\nPERFORM SIMPLE CALCULATIONS')
    a = input('Enter the first number: ')
    if not is_valid(a):
        print('Calculator stopped')
        break

    b = input('Enter the second number: ')
    if not is_valid(b):
        print('Calculator stopped')
        break

    operand = input(
        f'Pick an number:\n1 for {a} + {b}\n2 for {a} - {b}\n3 for {a} × {b}\n4 for {a} ÷ {b}\nYour choice: ')

    if not valid_choice(operand):
        print(f'"{operand}" is not a valid choice.\n Calculator stopped')
        break

    execute(a, b, operand)
    response = input(
        "\nEnter 'y' or 'yes' to perform another caculation or something else, to quit\nYour response: ")
    if quit(response):
        print('Bye!')
        break
