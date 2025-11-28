products = {
    'fruits':[('bananas',2,40),('skebobs',12,32)],
    'ovoshi':[('perchik',1,23)],
    'napitki':[('benzin',134,22),('solarka',35,12),('etanol',46,81)]
}
count = 0
print(f"максимальная цена в магазе:{max(products['fruits'][0][2], products['ovoshi'][0][2], products['napitki'][0][2] and products['fruits'][1][2], products['ovoshi'][1][2], products['napitki'][1][2])}")


UserChoice = input("vvedi categoriy")
for keys in products:
    if UserChoice == keys:
        print(products[keys])