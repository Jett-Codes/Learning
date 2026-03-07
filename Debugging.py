import pdb
#Debugging with prints
def add(a, b):
    result = a + b
    print(f"Adding '{a}' and '{b}' gives '{result}'") #allows you to check it all works
    return result
print(add(5, 7))

def divide(a, b):
    # pdb.set_trace() #allows pdb to check your code then in terminal enter help to see commands and debug code
    return a / b 
#using Pdb commands help with debugging such as whatis divide returns Function divide

#using continue or c allows the rest of the code to run
print(divide(10, 2))

#VS code debugger
def divide2(c, d):
    results = c / d #click the gutter(reddot) to indicate a breakpoint
    return results #start with debugging then it stops at breakpoint
#hover over variables to see values
# use variable panel to see ALL local variables
# debug console

print(divide2(10, 2))
print(divide2(15, 3))
#top of screen has things(step over exectutes the current line then moves)
# step into enter into function calls
# step out exits the current function

#try except else and finally blocks
try: #use where you think an error might occur
    x = 10 / 0
except ZeroDivisionError: #except runs if an error of the specified type is raised
    print("You cant divide by zero")
else: #runs if no exception is raised by try
    print("Division successful:", x)
finally:
    print("This block always runs") #runs no matter what whether or not an exception occured

try:
    s = 5 / '6'
except TypeError:
    print("Wrong type fam")
else:
    print('correct type:', s)
finally:
    print('This runs at the end no matter hwat')
#separating except clauses checks both to see which one may be causing problems
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')
#using e allows for putting it in your message

try:
    number = int(input('Enter Number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e: #allows input from person but not if someone puts something like a string or divides by 0
    print(f'Error occurred: {e}')
else: 
    print(result)

    #Raise Statements
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative') #raise allows you to bring in an exception at any point in your program 
    #this allows you to make your own rules and trigger exceptions like this
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') #Error age cannot be negative
 
#more things for raise
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except  ValueError:
        print('Logging: Invalid data received')
        raise #reraises the same value error

try: 
    process_data('abc')
except ValueError:
    print('Handled at higher level')
    #Future learn about classes 

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

    #Raise and from
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Config file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid config format') from e
#all happens in terminal
config = parse_config('config.txt')

def calculate_square_root(number): #Assert is shorthand raise with AssertionError
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')


