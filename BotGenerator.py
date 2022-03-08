from tkinter import *
import subprocess
import sys






root = Tk()
f = open("ApiDiscord.txt" ,"w")
root.geometry("800x800")
root.title("Bot generator")
e = Entry(root, width=200)
e.pack()
e.insert(0, "Put your api here! ")



def Clear():
    e.delete(0, END)


def Generate():
    api = e.get()
    with open("ApiDiscord.txt", "r+") as f:
        if api in f.read():
            print("It's already saved!")
        else:
            f.writelines(api + "\n")

    if len(api) > 59 or len(api) < 59:
        e.delete(0, END)
        e.insert(0, "You're api contains too much or not enought letters!")
    for i in api.split():
        if i.startswith('O'): #Checks if api starts with O, otherwise prints the error
            pass
        else:
            e.delete(0, END)
            e.insert(0, "Your api doesn't start with 'o'. Please try again!")
    spacje = sum(n.isspace() for n in e.get()) #Checks the amount of spaces
    if spacje > 0:
        e.delete(0, END)
        e.insert(0, "Your api can't have any spaces!")
    


    Bot = open("Bot.py","w")

    with open("Bot.py", "r+") as Bot:
        Bot.readlines("Will be done in the future")

    subprocess.run([sys.executable, "Bot.py"])








GenerateButton = Button(root, text = "Generate!", command = Generate).pack()
ClearButton = Button(root, text = "Clear", command=Clear).pack()



mainloop()
