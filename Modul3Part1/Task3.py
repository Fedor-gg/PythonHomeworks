num1 = int(input("<UNK> <UNK> <UNK> <UNK>"))
num2 = int(input("<UNK> <UNK> <UNK> <UNK>"))
numbers = range(num1, num2+1)
for number in numbers:
    if number % 3 == 0:
     print(f"{number} Fizz")
for number in numbers:
    if number % 5 == 0:
        print(f"{number} Buzz")
for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
         print(f"{number} FizzBuzz")
