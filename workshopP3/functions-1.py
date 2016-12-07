"""
lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower,upper))
for i in range(10, 120, 11):
          print("{} {}".format(i, chr(i)))
"""


def get_number(lower, upper):
    invaildValue = False
    user_input = 0
    while not invaildValue:
        try:
            user_input = int(input("Enter a number(10-50):"))
            if 50 > user_input > 10:
                invaildValue = True
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!?")
    return user_input
def main():
    print(value_num(get_number(10,50)))


def value_num(num):
    for i in range(0, 256, num):
        print("{:^8d} {:^8s}" .format(i, chr(i)))
main()
