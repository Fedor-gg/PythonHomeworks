data = input("text:")

with open('data/text.txt','w') as file:
    file.write(data)


file.close()