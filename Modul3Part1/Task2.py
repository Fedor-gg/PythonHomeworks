num1 = int(input("введите число:"))
num2 = int(input("введите число:"))
choice = input("1. Все числа диапазона;\n2. Все числа диапазона в убывающем порядке;\n3. Все числа, кратные 7;\n4. Количество чисел, кратных 5.")
numbers = range(num1, num2)

if choice == "1":
    for number in numbers:
        print(number)
elif choice == "2":
     for number in reversed(numbers):
         print(number)
elif choice == "3":
    for number in numbers:
        if number % 7 == 0:
            print(number)
elif choice == "4":
    count = 0
    for number in numbers:
        if number % 5 == 0:
         count += 1
    print(count)




