import json
from difflib import get_close_matches
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import sys

data = json.load(open("resources/binData.json"))

def callback(link):
    webbrowser.open_new_tab(link)

def Info():
    infoWindow = Tk()
    infoWindow.title("Info")
    
    infoWindow.geometry("300x200")
    infoWindow.minsize(300,200)
    infoWindow.maxsize(300,200)
    
    #Mali is Font Name here
    infoo1 = Label(infoWindow, 
                   justify=tk.CENTER ,
                   text="This app is developed by Abdul Rehman",
                   font='Mali 10 bold')
    infoo1.grid(row=0, column=0)
    infoo2 = Label(infoWindow, 
                   justify=tk.CENTER, 
                   text="Give feedback and Show support",
                   font='Mali 10 bold')
    infoo2.grid(row=1, column=0)

    eM = Label(infoWindow, 
               text="EMAIL: abdulrehmansarfaraz90@gmail.com")
    eM.grid(row=2, column=0)
    
    tw = Label(infoWindow, 
               text="   TWITTER:\n@itxHooman", justify=tk.LEFT)
    tw.grid(row=3, column=0)
    
    git = Label(infoWindow, 
               text="GITHUB:", justify=tk.LEFT)
    git.grid(row=4, column=0)
    
    'Hyperlink Method:'
    gitLink = Label(infoWindow, 
               text="www.github.com/Dev-Hooman", cursor='hand2', fg="blue")
    gitLink.grid(row=5, column=0)
    gitLink.bind("<Button-1>", lambda e: 
    callback("http://www.github.com/Dev-Hooman"))
    
    #infoWindow.iconphoto(False, tk.PhotoImage(file="icons_\INFO_2.png"))
    infoWindow.mainloop

window = Tk()
window.title("Dictionary")

window.geometry("406x428")
window.minsize(406,428)
window.maxsize(406,428)


def verify_and_Display(output):
    if(type(output) == list):
        for item in output:
            #this methed is for --> text.delete("clear arg", TILL END of the field)
            outBox.delete("1.0", END)
            outBox.insert(END, item)
    else:
        outBox.delete("1.0", END)
        outBox.insert(END, output)

def askQuestion():
    pop = Toplevel(window)

    def choice(op):

        if(op == "yes"):
            meaning = get_close_matches(GlobalShow, data.keys() )[0]

            verify_and_Display(data[meaning])
            pop.destroy()
            
        else:
            pop.destroy()
            tk.messagebox.showinfo(title= 'return', message='Sorry unable to find searched word, re-check it')


    pop.title('Wrong Input')
    pop.geometry("250x150")
    pop.minsize(250,150)
    pop.maxsize(250,150)
    pop.config(bg='white')

    global warnImage
    warnImage = PhotoImage(file = "resources/icons_/WARN.png")

    pop_label = Label(pop, text = 'Did you mean?' + " " + GlobalShow, bg = "white", fg= "black")
    pop_label.pack(pady=10)

    my_frame = Frame(pop, bg = "white")
    my_frame.pack(pady=5)

    GetImage = Label(my_frame, image=warnImage, borderwidth = 0)
    GetImage.grid(row=0, column = 0, padx=10)

    #lambda used to pass value outside the function
    yes = Button(my_frame, text ="YES", command=lambda: choice("yes"), bg ="orange")
    yes.grid(row=1, column=0)

    no = Button(my_frame, text ="NO", command=lambda: choice("no"), bg ="yellow")
    no.grid(row=1, column=1)

    pop.mainloop()

def dictionary(word):
    if(word in data):
        return data[word]

    elif(word.upper() in data):
        return data[word.upper()]

    elif(word.title() in data):
        return data[word.title()]

    elif(len(get_close_matches(word, data.keys())[0]) > 0):   #this fn is used to check incorrect words possibilites
        show = get_close_matches(word, data.keys() )[0]
        global GlobalShow
        GlobalShow = show
        askQuestion()
        #yesNo = tk.messagebox.askquestion(title = 'Wrong Input', message = 'Did you mean?' + " " + show , icon='warning')

window.iconphoto(False, tk.PhotoImage(file = "resources/icons_\ICON_1.png"))

Res = Label(window, text="\n RESULT", font=3)
Res.grid(row = 8, column = 3)

#for printing output of dictionary
outBox = Text(window, height=15, width= 50)
outBox.grid(row= 9, column = 3)

#first welcome label 
Header = Label(window, text="\n WELCOME TO DICTIONARY", font=8, fg="green")
Header.grid(row = 0, column = 3)

words = StringVar()
FirstEntry = Entry(window, textvariable = words, width=30)
FirstEntry.grid(row = 4, column = 3)

def dataEntry():
    wordsString = words.get()
    wordstored = wordsString.lower()
    output = dictionary(wordstored)
    verify_and_Display(output)

searchButton = Button(window, text="Search", command = dataEntry, bg='red', fg = 'white')
searchButton.grid(row=6, column=3)

def exitFn():
    window.quit()
    sys.exit()

#to exit application
exitButton = Button(window, text="   EXIT   ", command=exitFn)
exitButton.grid(row=11, column=3)

infoIcon = PhotoImage(file='resources/icons_\INFO.png')
myInfo = Button(window, command=Info, image=infoIcon, width=25, height=25)
myInfo.grid(row=12, column=3)

window.mainloop()

if __name__ == "__main__":
    dataEntry()
    