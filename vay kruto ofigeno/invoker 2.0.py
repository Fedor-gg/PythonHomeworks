spells=[]
while True:
    print('''main menu
    1-изучить калдавство
    2-списак калдавства
    3-тринировга
    4-юзнуть калдавство
    5-выход''')
    UserChoice = input()
    if UserChoice == '1':
        newSpel = input("какоэ калтафство исучит")
        if newSpel in spells:
            print("уже изучено")
        else:
            spells.append(newSpel)
            print("изучено")
    if UserChoice == '2':
        print(spells)
    if UserChoice == '3':
        newSpel = input("бро, тебе надо тренироваться")
        if newSpel in spells:
            for i in range(3):
                print(newSpel)
    if UserChoice == '4':
        newSpel = input("какое заклинание юзнуть?")
        if newSpel in spells:
            print("-99999hp")
        else:
            print("не изучено")
    if UserChoice == '5':
        print("все закругляйся")
        break
