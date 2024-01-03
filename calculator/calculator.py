#!/usr/bin/env python
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
		if (a%b) == 0:
			print(f'{a} ÷ {b} = {a//b}')
		else:
			print(f'{a} ÷ {b} = {a/b}')
	else:
		print('Error: invalid choice')

def is_valid(user_input):
	try:
		number = int(user_input.strip())
		return True
	except TypeError:
		print(f'{user_input} is not a number')
		return False
	except:
		print('Unknown Error!')

def valid_choice(choice):
	choice = choice.strip()
	options = [1, 2, 3, 4]
	
	for option in options:
		if option == int(choice):
			return True
		else:
			print('Invalid option')
			return False
			
def quit(response):
	options = ['y', 'yes']
	if response.strip().lower() in options:
		return False
	else:
		return True

while True:
	print('PERFORM SIMPLE CALCULATIONS')
	a = input('Enter the first number: ')
	if is_valid(a):
		b = input('Enter the second number: ')
	if is_valid(b):
		operand = input(f'Pick an number:\n1 for {a} + {b}\n2 for {a} - {b}\n3 for {a} × {b}\n4 for {a} ÷ {b}\n: ')
	
	if valid_choice(operand):
		execute(a, b, operand)
	response = input("Enter 'y' or 'yes' to perform another caculation or something else, to quit")
	if quit(response):
		break
		print('Bye!')
