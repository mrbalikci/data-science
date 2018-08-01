# booleans 

one_is_less_than_two = 1 < 2

print(one_is_less_than_two)

true_equals_false = True == False

print(true_equals_false)

# None is for nonexistent value 

x = None
print(x==None)
print(x is None)

## 

def some_funtion_that_returns_a_string():

    return str

s = some_funtion_that_returns_a_string()

# print(type(s))

if s:
    first_char = s[0]
    print(first_char)
else:
    first_char = ""
    print(first_char)