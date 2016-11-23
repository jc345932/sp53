"""
output_file = open("names.txt", "w")
user = input("What's your name?")
output_file.write("Your name is: {}\n".format(user))
output_file.close()
"""


input_file = open("numbers.txt", "r")
count = 0
for line in input_file:
    if count ==0:
        a = int(line)
        count +=1
    else:
        b = int(line)
        count +=2
print(a+b)