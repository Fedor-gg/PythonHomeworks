num1 = int(input("введите число"))
num2 = int(input("введите число"))
if num1 == num2:
    print("true")
elif num1 != num2:
    sorted_numbers = sorted([num1, num2])
    print(sorted_numbers)