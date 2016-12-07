"""
user_name = input("Enter the name: ")
while len(user_name) == 0:
    print("Invalid name")
    user_name = input("Enter the name: ")

for i in range(1,len(user_name),2):
    x = user_name[i]
    print(x, end = " ")
"""
def main():
    user_name = get_name()
    get_loop(user_name)


def get_name():
    user_name = input("Enter the name: ")
    while len(user_name) == 0:
        print("Invalid name")
        user_name = input("Enter the name: ")
    return user_name

def get_loop(user_name):
    for i in range(1, len(user_name), 2):
        x = user_name[i]
        print(x, end=" ")
main()

