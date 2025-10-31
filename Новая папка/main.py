import tkinter as tk
print("вам звонит покой в богатстве \n      принять???  отклонить.")
choice = str(input())
if choice == "принять":
    import webbrowser
    webbrowser.open("https://case-battle.life/")
if choice == "отклонить":
    asdf = tk.Tk()
    dfsa = tk.Label(text="у тебя и так не было выбора")
    dfsa.pack()
    asdf.mainloop()
