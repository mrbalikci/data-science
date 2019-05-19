### 
# default-dicts
###
document = ["i", "like", "everyone", "regardless", "of", "their", "color", "religion", "or", "etnicity", "i", 
"admire","everyone", "who", "respects", "others", "regardless","of","their","color","background", "and",
"religion"]

word_counts = {}

for word in document:
    if word in word_counts:
        word_counts[word] +=1
    else:
        word_counts[word] = 1

print(word_counts)

## or 

word_counts_2 = {}

for word in document:
    try:
        word_counts_2[word] +=1
    except:
        word_counts_2[word] = 1

print(word_counts_2)

# # get method 
word_counts_3 = {}
for word in document:
    previous_count = word_counts_3.get(word,0)
    word_counts_3[word] = previous_count + 1

print(word_counts_3)

# using defultdict

from collections import defaultdict

word_counts_4 = defaultdict(int)
print(word_counts_4)

for word in document:
    word_counts_4[word] +=1
print(word_counts_4)


dd_list = defaultdict(list)
print(dd_list)

dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"]= "Seattle"
print(dd_dict)