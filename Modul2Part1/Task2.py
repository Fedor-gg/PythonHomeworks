num1 = float(input("введите число:"))
num2 = float(input("введите число:"))
num3 = float(input("введите число:"))

choice = input("min or mid or max")

if choice == "min":
    print(min(num1, num2, num3))
elif choice == "mid":
    result1 = (num1 + num2 + num3) / 3
    print(f"mid: {result1}")
elif choice == "max":
    print(max(num1, num2, num3))

