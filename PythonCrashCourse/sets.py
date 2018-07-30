# collection of distinct elements 

s = set()
s.add(1)
s.add(2)
s.add(3)

print(s)

x = len(s)
print(x)

y = 2 in s
print(y)

z = 3 in s
print(z)

##
# set is most faster than a list 

item_list = [1, 2, 3, 4, 5]
num_items = len(item_list)
print(num_items)

item_set = set(item_list)
print(item_set)