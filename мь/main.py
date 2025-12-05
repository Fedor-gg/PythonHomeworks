data = str("лабуба лабубы лабубу бубубу бебебе")
try:
    file = open("text.txt", "w")
    file.write(data)
    file = open("text.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("меняй все")
except ValueError:
    print("что то стряслось")
    empty_symbol =len(lince.split)
    print(f"{empty_symbol}")
