# returns a new list 

x = [4, 2, 3, 1, 2]
y = sorted(x)
print(y)

print(x.sort())

# sort by abs value largest to smallest 
z = sorted([-4, -5, 3, -2, 0, 1, 2, -1], key=abs, reverse=True)
print(z)

document = ["i", "like", "everyone", "regardless", "of", "their", "color", "religion", "or", "etnicity", "i", 
"admire","everyone", "who", "respects", "others", "regardless","of","their","color","background", "and",
"religion"]

word_counts = Counter(document)
print(word_counts)

for word, count in word_counts.most_common(3):
    print(word,count)

# sort the words 
wc = sorted(word_counts.items(), key=lambda, (word, count): count, reverse=True)
    
print(wc)
