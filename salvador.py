#Calculator Jan 23, 2024 (Programming Languages)


is_exit = False

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mult(a, b):
	return a * b

def div(a, b):
	return a / b

while is_exit == False:

    user_input = input('choose (add, sub, mult, div, exit: )')
    if user_input == 'exit':
    	break

    first_input = int(input('Enter value: '))
    second_input = int(input('Enter value: '))

    if user_input == 'add':
    	total = add(first_input, second_input)
    	print(total)

    elif user_input == 'sub':
    	difference = sub(first_input, second_input)
    	print(difference)

    elif user_input == 'mult':
    	product = mult(first_input, second_input)
    	print(product)

    elif user_input == 'div':
    	quotient = div(first_input, second_input)
    	print(quotient)

    else:
    	print('invalid') 