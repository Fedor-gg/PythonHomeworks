while True:
    spells = []
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
        print('''1-рывок скебоба
        2-банановый флип флоп
        3-отрыжка мистера крабса''')
    if UserChoice == '3':
        print('''че тренить бро?
        1-рывок скебоба
        2-банановый флип флоп
        3-отрыжка мистера крабса''')
        if UserChoice == '1':
            for spell in range(3):
                print(spell)
        elif UserChoice == '2':
            for spell in range(3):
                print(spell)
        elif UserChoice == '3':
            for spell in range(3):
                print(spell)
    if UserChoice == '4':
        print('''какое заклинание юзнуть?
                1-рывок скебоба
                2-банановый флип флоп
                3-отрыжка мистера крабса''')
        spell = input()
        for spell in spells:
            print("крутой, заюзал")





