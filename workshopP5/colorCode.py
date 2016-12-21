COLOR_NAMES = {"AliceBlue":"#f0f8ff","WHEAT":"#f5deb3","GRAY68":"#adadad","SEAGREEN3":"#43CD80"}
color = str(input("Enter your color: ")).upper()
while color != "":
    if color in COLOR_NAMES:
        print(COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = str(input("Enter your color: ")).upper()