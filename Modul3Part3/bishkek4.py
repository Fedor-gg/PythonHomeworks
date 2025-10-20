number = int(input())
strNumber = str(number)
newNumber = ""
for number in strNumber:
    if number != "3" and number != "6":
        newNumber += number
print(newNumber)


