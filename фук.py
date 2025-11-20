import random
while True:
    random_word = ['Cold Snap', 'Ghost Walk', 'Ice Wall', 'EMP', 'Tornado', 'Alacrity', 'Deafening Blast', 'Sun Strike', 'Forge Spirit', 'Chaos Meteor']
    word = random.choice(random_word)
    UserChoice_list = ['qqq', 'qqw', 'qqe', 'www', 'wwq', 'eew', 'qwe', 'eee', 'eeq', 'wwe']
    print(random.choice(random_word))
    UserChoice = input("Enter combination: ")
    if random_word == 'Cold Snap' and UserChoice == 'qqq':
        print("nice")
    elif random_word == 'Cold Snap' and UserChoice != 'qqq':
        print("nope")
#НЕ ТРОГАЙТЕ КОД!!!!!!

