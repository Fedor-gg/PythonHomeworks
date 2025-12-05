x = 0
while x == 0:
    try:
        x = int(input("lslle"))
        x += 5
        print(x)
    except ValueError:
        print("Enter a number")


#_____________________________________________________________________

try:
    x = 5 / 0
    x = int(input("lslle"))
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("che to ne to")
else:
    print("else")
finally:
    print("fin")


