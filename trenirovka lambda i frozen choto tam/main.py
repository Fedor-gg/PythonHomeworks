def test_function(word):
    print(word, end="")
    print("!")
test_function("hui")



def summa(a, b):
    res = a+b
    return res
    print("result:", res)
summa(5.5,3.3)
#summa("h","i")

#data =set('hello')
data = {5,3,5,6,3,1}
data.add(31)
data.update({'True', False,4,6})
data.remove(False)
data.pop()
#data.clear()
nums = [5,3,2,1,4,5]
new_nums = set(nums)
new_data = frozenset([3,5,2,1,'31',True,4,2,1,5,2])
print(data)
