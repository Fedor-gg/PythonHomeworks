num = float(input("введите число"))

choice = input("inches or miles or yards")

if choice == "miles":
    result1 = num * 0.000621371
    print(f"miles: {result1}")
elif choice == "inches":
    result2 = num * 39.3701
    print(f"inches: {result2}")
elif choice == "yards":
    result3 = num * 1.09361
    print(f"yards: {result3}")
else:
    print("ошибка ввода")
