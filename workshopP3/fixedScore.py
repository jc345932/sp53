"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def get_score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    print(get_score(float(input("Enter score: "))))

main()
