# import math as mt can do this but can only take some like
# from math import radians, sin, cos
#and finally 
from math import* 
#you want to import everything but dont want to use math.(function name)
import datetime


# dictionary = {
#     key1: value1, Dictionary steps such as storying variables and assigning them
#     key2:value2
# }

pizza = { #dictionary {}
    'n': 'Pepperoni pizza', #variable name: value Pepperoni pizza
    'price': 10.9, #variable price:  value 10.9
    'calories': 250, #variable calories: value 250
    'toppings': ['cheese', 'Pepperoni'] #variable toppings: value cheese and pepperoni
}

#another way
pizza2 = dict([('name', 'Cheese pizza'), ('Price', 8.9), ('calories', 200), ('toppings', ['Sauce', 'Cheese'])])
#list of tuples in the brackets or tuples in the list 
#dictionary[key] access a variable
pizza2['name'] # Cheese Pizza
print(pizza2['name']) #prints cheese pizza
pizza2['name'] = 'Cheese' # name changes to cheese for the second dictionary
print(pizza2['name']) #prints Cheese

#.get retrieves the values associated with a key dictionary.get(key, [default])
print(pizza.get('calories', [])) #prints 250

#respectively .keys() gets the keys and .value() gets the value and .items() get both
print(pizza.keys()) #prints all keys or variables
print(pizza.values()) #prints all of pizzas values 
print(pizza.items()) #prints both together
#.clear() clears it all
#.pop(0 removes key value pair)
# print(pizza.pop('name')) #removes the name and value
pizza.pop('name', 'Pepperoni pizza') # removes the name
print(pizza.items()) #doesnt print name
print(pizza.pop('name', 'Pepperoni pizza')) #returns the value only since key doesnt exist
# print(pizza.pop('name')) #key error as it doesnt have a value and key doesnt exist
#popitem
print(pizza2.popitem()) #removes the last listed key value pair but shows what item it removed
print(pizza2) #shows everything but removed
pizza = { #reintroduce
    'name': 'Pepperoni pizza', #variable name: value Pepperoni pizza
    'price': 10.9, #variable price:  value 10.9
    'calories': 250, #variable calories: value 250
    'toppings': ['cheese', 'Pepperoni'] #variable toppings: value cheese and pepperoni
}
#.update()
pizza.update({'price': 15, 'total_time': 25}) #updates the price key item pair and adds the total time key item pair
print(pizza)

#common techniques to loop over a dictionary
products = {
    'Laptop': 990,
    'Phone': 1300,
    'Ipad': 800,
    'Headphones': 100,
}
for price in products.values(): #loops over the dictionary then prints the only values
    print(price) #prints all values
for product in products.keys():
    print(product)
#or
for product in products:
    print(product) #prints same response of all keys

for product in products.items():
    print(product)

for product, price in products.items(): #each variable product and price hold its own value in the .items() since the .items has 2 things
    print(product, price)

for product,price in products.items():
    products[product] = round(price * 0.8) #rounds it to nearest whole number but is 20%
# this means the value of product or the key product value is price * .8 
print(products)

for product in enumerate(products):
    print(product) #numbers off all products of keys keeps it in tuples
for index, product in enumerate(products):
    print(index, product) #unpacks the tuples

for price in enumerate(products.values()):
    print(price) #lists off the prices in tuples
for index, price in enumerate(products.values()):
    print(index, price) #lists off the prices in not tuples
for index, product in enumerate(products.items()):
    print(index, product) #lists off everything in the dictionary 

#now
for index, product in enumerate(products.items(), 1): #starts it at 1
    print(index, product)

#Sets
my_set = {1, 2, 3, 4, 5}
# set()
# {} dictionary
my_set.add(6) #adds 6 to the end
my_set.add(5) #changes nothing since 5 is already there

my_set.discard(4) #removes the 4 but if its not there no key error
my_set.remove(5) #removes the 5 but if its not there yes Keyerror
print(my_set)
my_set = {1, 2, 3, 4, 5,}
your_set = {2, 4, 6}

#super and subsets
print(your_set.issubset(my_set)) #false since they dont share the same elemts
print(my_set.issuperset(your_set)) #false for same reason
#disjoint means no elements in common
print(my_set.isdisjoint(your_set)) #false as they have some elements in common
#union  | returns a new set with 2 sets data
print(my_set | your_set) #{1, 2, 3, 4, 5, 6}

print(my_set & your_set) #only elements the set have in common
print(my_set - your_set) #only what elements in the first set are not all the second
print(my_set ^ your_set) #only in one or the other so if 2 was in the first and not second it would return
# |= &= -= ^= all these do the same but update the first set used
my_set -= your_set #updates my_set to have {1, 3, 5}
print(my_set)
#checking with in
print(5 in my_set) #returns true or false so here true

# Modules and importing them

#top of code imported math
# mt.sqrt(36) can now do this but
#can also import not a bunch of things 
angle = 40
angle_rad = radians(angle)

sin_value = sin(angle_rad)
cos_value = cos(angle_rad)

print(sin_value) #.6427876096865393
print(cos_value) #.766044443118978
#import date time
birthday = datetime.date(2010, 8, 1)
print(birthday.day)
print(birthday.month)
print(birthday.year)
#name thing
if __name__ == "__main__":
    print("This is the main code") #this will not print but everything else will if this was imported to another code

Testing = {
    'testing': 'Values',
    'Hello': 'world',
    'Goodbye': 'Worlds'
}
def add_setting(settings, keys):
    key = keys[0].lower()
    print(key)