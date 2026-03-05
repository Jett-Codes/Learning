
cities = ['Los Angeles', 'Kyoto', 'London']
cities[0] #Los Angeles
cities[-2] #Kyoto
developer = 'Jettslinger'
list(developer) #J e t t s l i n g e r
len(cities) #3 for the 3 things in the list
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript' #replaces the first one
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']
del programming_languages[1] #removes java
print(programming_languages)
'Rust' in programming_languages # True
'Java' in programming_languages # False
listinlist = ['Diddy', 'Deagan', ['Python', 'Java', 'C++', 'Rust']]
listinlist[2] #gives the other list
print(listinlist[2][1]) #other list with the second one in that list
dihveloper = ['Jett', 15, 'Boi'] 
name, age, boi = dihveloper # unpacks list
print(name)
print(age)
print(boi)
veloper = ['Jett', 15, 'Boi']
name, *rest = veloper #* gets the rest other than the name
print(name)
print(rest) 
#if too many variables on left side it will be an error
dessert = ['Cake', 'Brownie', 'Icecream', 'Cookie']
dessert[1:3] # [Brownie, Icecream, cookie] splits
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] #only has every 2
numbers.append(7) #adds 7
print(numbers)
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
odd.append(even) #adds odd
print(odd)
number = [1 , 3, 5]
number1 = [2, 4, 6]
number.extend(number1)
print(number)
diddy = [1, 2, 3, 5]
diddy.insert(3, 4)
print(diddy) #inserts it somehow to be [1, 2, 3, 4, 5]
epstien = [10, 20, 30, 40, 40, 50]
epstien.remove(40) #removes first instince of the number
print(epstien)
drake = [1, 2, 3, 4, 5]
drake.pop(2) #takes third instint so 3 is returned/removed 
#if pop() left alone it removes last thing in list
print(drake)
#if .clear() used list is cleared
trump = [19, 4, 5, 2, 7]
trump.sort() #sorts all numbers
print(trump)
#can make another variable with sorted(insert old variable here) to make a new one that is sorted 
johnny = [6, 5, 4, 3, 2, 1]
johnny.reverse() #reverses order
print(johnny)
print(johnny.index(4)) #3 shows what number your element is in a list
#if no element found = value error
#Tuple like lists but can not be changed out side
Tuple1 = ('Jett', 'Tanner', 'Esslinger')
print(Tuple1)
# Tuple1[0] = 'John' gives an error since you cant change it 
Tuple1[0] #Jett this is how you get the element
print(Tuple1[0])
# Tuple1[7] if it goes over how many elements = IndexError
Create = 'Jett'
tuple(Create) #gives (J, e, t, t)  this is how you create a tuple
print(tuple(Create))
#to check if in tuple use in command
'Jett' in Tuple1 #True
print('Jett' in Tuple1)
#unpacking
first, middle, last = Tuple1 #takes the 3 elements and unpacks them into these names
print(first) #Jett
print(middle)#Tanner
print(last) #Esslinger
# * collects leftover elements                                                      
first, *rest = Tuple1 #checks first then makes the leftover go into rest
print(first) #Jett
print(rest) #[Tanner, Esslinger]
#can use slice on tuples also
Tuple1[1:2] #prints [Tanner] as second number is not included
# cannot remove from Tuples
# del Tuple1[1] gives error since no changes can be made
# use list when you might need to change
# Tuple when you dont need to change

# common tuple methods
Tuple2 = ('Gyro', 'Diego', 'HotPants', 'Poccoloco', 'Gyro')
Tuple2.count('Gyro') #2
Tuple2.count('Johnny') #0
# Count sees how many times it appears in the tuple
#  if Tuple2.count() would give type error since nothing is inputed
Tuple2.index('Diego') #where in the tuple it is so 1
#if its not in the tuple Value error
Tuple2.index('Gyro', 2) #skips over the first one since 2 is the starting point
#prints 4
Tuple2.index('Gyro', 0, 4) #starts at zero but stops before 4 not including it 
# prints 0
num = (1, 4, 3, 67, 2)
sorted(num) #sorts them into a LIST
sorted(Tuple1, key=len) #sorts by length
print(sorted(Tuple1, key=len, reverse=True)) #Len goes shortest to largest while reverse reverses that
#['Esslinger', 'Tanner', 'Jett'] is what is printed


# Loop time
Loop1 = ['spin', 'Hamon', 'Stands']
Loop2 = ['Apple', 'Bannana']

#For loop
for technique in Loop1: 
    print(technique) #must be indented
# prints
#spin
#hamon
#stands
for char in 'Spin':
    print(char) #prints all letters down each line

for food in Loop2:
    for tech in Loop1:
        print(food, tech) # prints one food for until the tech is done then repeats this is called nesting
# Apple spin
# Apple Hamon
# Apple Stands
# Bannana spin
# Bannana Hamon
# Bannana Stands


# While Loops

secret = 4
guess = 0

while guess != secret: #while the number you guess is not secret or True this loops
    guess = int(input('Guess the number (1-5): ')) #input allows you to guess a number needs int to convert input string
    if guess != secret: #if wrong reloops
        print('wrong try again.')
print('you got it') #if right loop ends you break free

# break statement
for techs in Loop1: 
    if techs == 'Hamon': #if it goes down list and is Hamon
        break #Ends right then and there
    print(techs) #only prints the first one

for techs in Loop1:
    if techs == 'Hamon':
        continue #skips whatever it equals
    print(techs)    

for word in Loop1: #checks every word in the list
    for letter in word: #checks the letters in every word
        if letter.lower() in 'aeiou': #sees if they are these letters
            print(f"'{word}' 'has the vowels' '{letter}'") #if they are prints this {word} is just the 1st,2nd, or 3rd word
            break #when it does break out of inner loop and repeat
    else: #if it doesnt contain vowels goes down here before looping
            print(f"'{word}' has no vowels")
# finishes when everything was checked


#Ranges and loops
# range(start, stop, step) 
for num in range(3): #3 is not included and stops there because stop is non inclusive
    print(num)

for num in range(1, 5): #starts at 1 and goes to 4 because stops at 5 and 5 is non inclusive
    print(num)

for num in range(2, 11, 2): #starts at 2 goes up in STEPS of 2 until 10 since 11 is not included
    print(num)
#if range() has nothing type error is up or range(.5) only ints no floats=decimals

for num in range(40, 0, -10): #starts at 40 and goes down in 10s or -10 and doenst reach 0
    print(num)
numbers = list(range(2, 11, 2)) #creates list of ints
print(numbers) #[2, 4, 6, 8, 10]

#Enumerate and Zips 

languages = ['Spanish', 'english', 'Japanese', 'Chinese']

for lang in languages:
    print(lang)

index = 0

for lang in languages:
    print(f'Index {index} and language {lang}') #every loop checks the index and numbers them
    index += 1 #HERE

#Enumerate comes in
print(list(enumerate(languages))) #makes it tuples in a list with an index count
#[(0, 'Spanish'), (1, 'english'), (2, 'Japanese'), (3, 'Chinese')]

for index, lang in enumerate(languages): #unpacks the count and value for each tuple in the enumerate object
    print(f'Index {index} and languages {lang}') #no need for index variable
#since in a normal enumerate it goes index then the number the values we named take that same route
for index, lang in enumerate(languages, 1): #makes it start at 1
    print(f'Index {index} and languages {lang}')

#ZIP function  

ids = [1, 2, 3, 4]

list(zip(languages, ids)) #makes it a list then zips up the two or more things into tuples in the order displayed
print(list(zip(languages, ids))) #[('Spanish', 1), ('english', 2), ('Japanese', 3), ('Chinese', 4)]

for lang, id in zip(languages, ids): #lang, is matched with languages, and id is matched with ids
    print(f'Language: {lang}') # = and languages in the list
    print(f'ID: {id}') # = all ids in the id list

#List comp useful function with lists

even_numbers = []

for num in range(21): #makes a list of numbs 0-20
    if num % 2 == 0: #if number has remainder 0 when divided by 2 finds out if even
        even_numbers.append(num) #appended adds to end of list so first number there is 0 but eventually moved up the list
print(even_numbers)#all numbers appended leaves loop boom
even_numbers = [num for num in range(21) if num % 2 == 0] #first num is what expression or what will be in the new list
print(even_numbers) #second num is the loop variable in range(21) if divided by 2 and remainded 0 add it to the first num
numbers1 = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers1]
print(result)
#result is num, 'even if number is divisible by2 else its odd num in number gives variable and all this in brakets is tuple
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word): #word is parameter or placeholder
    return len(word) > 4 #checks the length of the word in int then sees if it is more than 4
#if so returns it
long_words = list(filter(is_long_word, words)) #filter is used to only let words through if they meet criteria
print(long_words) 
#filter checks each word in words then is_long_word takes that and uses its function to check it
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius)) #map takes iterable and adds function to each of its elements 
print(fahrenheit)
#map is how each of the elements in the list go to fahrenheit
numbers2 = [5, 10, 15, 20]
total = sum(numbers2) #adds all up from list or tuple
print(total)

total2 = sum(numbers2, 10) #starts at 10 then adds on
print(total2)


# Lambda functions

def square(num):
    return num ** 2 #** ^ whatever
print(square(4)) #16

lambda num: num ** 2  #lambda is anonymous function so no name
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #parameter: expression
print(even_numbers)  # [2, 4]
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers)
