group = {}

text = input("Please enter text:")
words = text.split(" ")

for word in words:
    if word not in group:
        group[word] = 1
    else:
        group[word] +=1
for word in sorted(group):
    print(word, ":", group[word])