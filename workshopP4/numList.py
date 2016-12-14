list = []
for i in range(5):
    num = int(input("Enter the number: "))
    list.append(num)

print("The first number is: ",list[0])
print("the last number is: ", list[-1])
print("the smallest number is: ", min(list))
print("the largest number is: ",max(list))
print("the average of the numbers is: ",sum(list)/len(list))
