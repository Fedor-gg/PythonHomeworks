import random
count = 0
list = [random.randint(-100,100) for i in range(10)]
print(list)
negative_count = sum(1 for num in list if num <0)
positive_count = sum(1 for num in list if num >0)
zero_count = sum (1 for num in list if num == 0)
print(min(list), max(list))
print(negative_count, positive_count, zero_count)