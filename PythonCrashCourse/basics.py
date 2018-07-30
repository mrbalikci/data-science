# for i in [1,2,3,4,5]:
#     print(i)
#     for j in [1,2,3,4,5]:
#         print(j)
#         print(i+j)
# print('done looping')

# # modules 

# import re 
# my_regex = re.compile("[0-9]", re.I)
# print(my_regex)

# print(5//2)
# print(5/2)

# # functions 

def double(x):
    return x*2

print(double(10))

def apply_to_one(f):
    return f(1)


my_double = double
x = apply_to_one(my_double)
print(x)

y = apply_to_one(lambda x:x+5)
print(y)

def my_print(message="this is my message"):
    print(message)
my_print("hello")
my_print()

print("hey")


####
print("####")

def substract(a=0, b=0):
    return a-b
print(substract())
print(substract(10,5))

print("####")

###
# Strings 
###

multi_strings = """ This is Erdem. 
and he lives in Austin. 
he is from Kurdistan"""

print(multi_strings)

###
# Exceptions 
###

try: 
    print(0/0)
except ZeroDivisionError:
    print('Everything is allright')


### 
# Lists
### 
integer_list = [1, 2, 3]
print(sum(integer_list))

x = range(10)
print(x)
print(x[1])

print(x[-3:])
print(x[1:-1])

print(10 in range(10))

###

x = [1, 2, 3]

x.extend([4, 5, 6])
print(x)

x.append(100)

print(x)

### 
# unpacking 
###

x, y, z = [1,2, 3]
print(y)

_,y = [1,3]
print(y)

### 
# Tuples 
### 

def sum_and_product(x,y):
    return(x+y),(x*y)

print(sum_and_product(3,5))


a, b = sum_and_product(10, -5)
print(a,b)

### 
# Dictionaries 
### 
grades = {"Erdem":100, "Birkan":95}

erdem_grades = grades["Erdem"]
print(erdem_grades)

try:
    volkan_grade = grades["Volkan"]
except:
    print("No Grade for Volkan!")

erdem_has_grade = "Erdem" in grades
print(erdem_has_grade)

erdem_grades = grades.get("Erdem", 0)
print(erdem_grades)

one_one_grades = grades.get("No One")
print(one_one_grades)

grades['Serkan']=99
grades['Arif']=89
grades['Hatice']=93

print(grades)

print(len(grades))

tweet = {
    "user": "drilldata",
    "text": "data is the new oil!",
    "retweet_count":103,
    "hastags": ["#data", "#oil"]
}

tweet_keys = tweet.keys()
print(tweet_keys)

tweet_values = tweet.values()
print(tweet_values)

tweet_items = tweet.items()
print(tweet_items)

print("user" in tweet_keys)
print("user" in tweet)