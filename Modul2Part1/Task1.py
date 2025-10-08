
num1 = float(input("введите число:")) #флот потому что предусматриваем разные значения чисел
num2 = float(input("введите число:"))
num3 = float(input("введите число:"))
choice = input("sum or product:")
if choice == "sum":
    result1 = (num1 + num2 + num3)
    print(f"sum = {result1}")
elif choice == "product":
    result2 = (num1 * num2 * num3)
    print(f"product = {result2}")
else:
    print("неверно")



