# in most progragramming language 

if 1>2:
    message = "if only 1 were than two..."
    print(message)
elif 1 > 3:
    message = "elif stands for 'else if'"
    print(message)
else: 
    message = "when all else fails use else"
    print(message)

x = 5
parity = "even" if x % 2 == 0 else "odd"
print(parity)

# while loop

x = 0
while x < 10:
    print(x, "is less than 10")
    x +=1

# for loop
for x in range(10):
    print(x, "is less than 10")

# more complex 
for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

