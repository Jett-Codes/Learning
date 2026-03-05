name = 'Jett Tanner Esslinger' #strings
Address = 'E Redwick Drive'
Address_Number = 1246 #int
age = 15.5 #float
gay = True #bool
dictionary = {'diddy', 'epstien', 'me'} #dictionary is multiple things
numbertop = (6, 37, 24) #tuple: An immutable ordered collection, enclosed in brackets, like 
count = range(5) #Range: A sequence of numbers, often used in loops, for example, range(5).
topthings = ['basses', 'deagan', 37, 'cats']  #List: An ordered collection of elements that supports different data types.
nothing = None #None: A special value that represents the absence of a value.
multiline = """multi 
line
diddy""" #multiline allows it to go into different line
test1 = 'It\'s sunny' #if single quotes \ escapes the string so it can print the ' in it's
test2 = "It's sunny" #if double quotes no \ needed
print(name, 'lives at', Address_Number, Address, 'is', age, 'and gay', gay, 'top 3 people', dictionary, 'top numbers', numbertop, count, topthings, nothing, multiline)
print(type(name)) #tells what class it is
print(type(Address))
print(type(Address_Number))
print(type(age))
print(type(gay))
print(type(dictionary))
print(type(numbertop))
print(type(count)) 
print(type(topthings))
print(type(nothing))
isinstance(name, str) #tells if the variable you say it is is it so this true
print(test1)
print(test2) # prints same thing
print('Redwick' in Address) #sees if these characters are in the string so this should be true
print('W' in Address) # this should be false makes it boolean
print(len(Address)) # says how many characters are in ts 
print(Address[3]) # sees what the letter is in the 3rd character space 
print(Address[-1]) # sees one from the last
Added_strings = name + ' ' + Address 
print(Added_strings) #can only do this with strings
# if str + int is error but
Address_added = str(Address_Number) + ' ' + Address #must make it a string
print(Address_added)
name_and_age = name  
name_and_age += str(age)
print(name_and_age)
age_name = f'My Name is {name} and i am {age}' #f function allows you to {put variables in these} so you can easily print
print(age_name)
#string[start:stop] start and stop need to be defined in numbers 
print(name[1:4]) #ett using the 1-4 characters in the str 1 is the second character since 0 exists
print(name[:9]) #goes from zero to nine but not including
print(name[9:]) #goes from 9 to the end
print(name[:]) #full str
print(name[0:19:3]) #goes full thing but removes every 3 letters
print(name[::-1]) #lowk flips it all inverse
uppercase_name = name.upper() #makes all uppercase
print(uppercase_name) 
lowercase_name = uppercase_name.lower() #makes all lowercase
print(lowercase_name)
test = '  hello diddy   '
print(test)
trailing_remover = test.strip() #strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
print(trailing_remover)
 #replace(old, new): Returns a new string with all occurrences of old replaced by new.
replace_name = name.replace('Jett', 'Ett' )
print(replace_name)
split_name = name.split()
print(split_name)
join_thing = ', '.join(dictionary) #joins dictionary to one string
print(join_thing)
start_with = name.startswith('Jett')
print(start_with) #creates bool sees if starts with Jett
end_with = name.endswith("Esslinger")
print(end_with)
index = name.find('Tanner') #what number it is in the string so jett is 4 so tanner starts at 5
print(index) #5
e_count = name.count('e')
print(e_count) #counts how many e's there are.
is_upper = name.isupper()
print(is_upper) #checks if all letter are upper case is bool
capit = name.capitalize()
print(capit) #capitalizes first letter
is_lower = name.islower()
print(is_lower)
title_alert = name.title()
print(title_alert) #capitalized all first letters
#ints and floats stuff
numb1 = 12
numb2 = 45
print(numb2 - numb1) # subtraction
print(numb1 * numb2) #multiplication
print(numb2 / numb1) #division
addedNumb = numb1 + numb2
print(addedNumb) #addition
flota1 = 12.3
flota2 = 43.1
print(flota1 - flota2) #subtraction of floats
print(flota1 * flota2) #multiplication
print(flota1 / flota2) #division
print(flota1 + flota2) #add
#float and int added is float in the end
float_intadd = flota1 + numb1
float_intsub = flota1 - numb1
float_intdiv = flota1 / numb1
float_intmult = flota1 * numb1
print(float_intadd)
print(float_intdiv)
print(float_intmult)
print(float_intsub)
#(%) returns the remainder when the value on the left is divided by the value on the right:
float_remain = flota1 % flota2 #can do the same with int
print(float_remain)
#Floor division divides two numbers and returns the greatest integer
# less than or equal to the result. This is done with the double forward slash operator (//):
float_floor = flota1 // flota2
print(float_floor)
#Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**):
float_exp = flota1 ** flota2
print(float_exp)
#how we can change variables
floattoint = float(numb1)
inttofloat = int(flota1) 
print(inttofloat)
print(floattoint)
string1 = '45'
stringtofloat = float(string1)
print(stringtofloat)
my_int_1 = 46.5243
#round() rounds it all
convert_int = round(my_int_1)
print(convert_int) 
num = -15
numabs = abs(num) #absolute value
print(numabs)
power = pow(5,3) #raises first to power of second
print(power)
myvar = 10
myvar += 5
print(myvar) # += adds onto a int
# you can also do -= *= /= The floor division operator (//=) floor‑divides the left variable by the right and stores the result back in the left variable:
#The modulus assignment operator (%=) computes the remainder of the left variable divided by the right and stores it back in the left variable:
#The exponentiation assignment operator (**=) raises the left variable to the power of the right and stores the result back in the left variable:
#you can also do this with strings 
greet = 'hello'
#greet += '  world'     
#print(greet) prints hello world
greet *= 3
print(greet) #now equals hello 3 times so hello hello hello
#cant divide or subtract though
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
#if condition:
 #   pass # Code to execute if condition is True
Jett = False
if Jett: #asking if jett = true
    if age >= 15.5: #if means in this is true the do this but second line must have indent
        print('you are old as hell')
else:
    print('you young boi') 
    #elif age == 15.5: #elif is else if you can use how many as
 #   print('bro is Jett years old ')
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
print(Jett and age) #since jett is true it prints age if jett was false it would not and instead print false
if Jett and age == 15.5:
    print('Bro is Jett Tanner Esslinger')
# or checks if it one or the other
if age == 15.5 or Jett:
#print('thinks he is Jett by name or age')
#print(not '') # True, because empty string is falsy
#print(not 'Hello') # False, because non-empty string is truthy
#print(not 0) # True, because 0 is falsy
#print(not 1) # False, because 1 is truthy
#print(not False) # True, because False is falsy
#print(not True) # False, because True is truthy
 if not Jett:
    print('Bro is not jett')
else:
    print('bro is jett')
    #INPUT TIME
name = input('what is your name?')
print('Hello', name)
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
def hello():
   print('Hello World') #def allows you to make your own function
hello()
def calc(a, b): #makes a function using a and b
   print(a + b) # allows function to print with a + b 
calc(4, 5) #shows you can use a and b as a variable so you can change it
my_sum = calc(4, 5)
print(my_sum) # none
def calc1(a, b):
   return a + b # must use return to return results
calc1(4,5) 
my_sumreal = calc1(4,5)
print(my_sumreal)
def my_func():
    my_var = 10
    print(my_var) #cant print my_var outside the my_func thing
def outer_func():
    msg = 'Hello there!'
    res = ''

    def inner_func():
        nonlocal res
        res = 'This wont print since its inner unless localized'
        print(msg)

    inner_func()
    print(res)

outer_func() # Hello there!
my_var = 100

def show_var():
   print(my_var)

show_var() #prints 100
print(my_var) #prints 100 
my_var_1 = 7

def show_var1():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_var1()

print(my_var_2) # my_var_2 is now a global variable and can be accessed anywhere in the program

def change_var():
   global my_var_1
   my_var_1 = 10

change_var()

print(my_var_1)
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
