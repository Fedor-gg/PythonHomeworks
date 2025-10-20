count = 0
for number in range(100, 999+1):
    number = str(number)
    if number[0] == number[1] or number[2] == number[1] or number[0] == number[2]:
        count += 1
        print(count)
