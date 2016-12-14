import random

pick = int(input("How many quick picks?"))
for y in range(pick):
    lottery =[]
    for i in range(6):
        num = True
        while num:
            number = random.randint(1,45)
            if number not in lottery:
                lottery.append(number)
                num = False
        lottery.sort()
    print(lottery)