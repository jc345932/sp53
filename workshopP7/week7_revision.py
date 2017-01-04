words = ['John', 'Jane', 'John']
counts_dict = {} #{"John":2, "Jsnr":1}
for word in words:
    try:
        counts_dict[word] += 1
    except KeyError:
        counts_dict[word] = 1
    print(counts_dict)


x = 10
y =9.9
z = "abc"
print(type(x))
print(type(y))
print(type(z))