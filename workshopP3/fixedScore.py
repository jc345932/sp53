"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invald score")
else:
    if score > 100:
        print("Invaild score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    elif score < 50:
        print("Bad")