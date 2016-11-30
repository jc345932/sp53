""""
value = 'Value'
character = 'Char'
print("{:^8s} {:^8s}" .format(value, character))
for i in range (0, 256):
    print("{:^8d} {:^8s}" .format(i, chr(i)))
"""



def get_number(lower, upper):
    user_input = int(input("Enter a number:"))
    if lower > user_input:
        print("Please enter a valid number!")
    if upper < user_input:
        print("Please enter a valid number!")
    return user_input
def main():
    user_num = get_number(10, 50)
    print("{:^6} {:^6}" .format(user_num, chr(user_num)))
    for i in range (10, 50):
        print("{:^8d} {:^8s}" .format(i, chr(i)))
main()