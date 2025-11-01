import webbrowser
print("хорошее настроение?")
choice = str(input())
if choice == "да" or choice == "Да":
    webbrowser.open("https://www.dota2.com/home")
elif choice == "нет" or choice == "Нет":
    print("ок")
else:
    print("ну ответь да или нет балбес")