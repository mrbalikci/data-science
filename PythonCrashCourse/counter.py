from collections import Counter

c = Counter([0,1,2,0])

print(c)

document = ["i", "like", "everyone", "regardless", "of", "their", "color", "religion", "or", "etnicity", "i", 
"admire","everyone", "who", "respects", "others", "regardless","of","their","color","background", "and",
"religion"]

word_counts = Counter(document)
print(word_counts)

for word, count in word_counts.most_common(3):
    print(word,count)


