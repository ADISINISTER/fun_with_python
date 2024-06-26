from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text ="type", src ="English", dest ="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Google Translator")
root.geometry("400x500")
root.config(bg="blue")

lab_txt = Label(root,text = "Translator", font=("Times New Roman",30,"bold"), bg="yellow")
lab_txt.place(x=80, y=10, height=55, width=250)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text = "Source Text", font=("Times New Roman",20,"bold"), fg="red")
lab_txt.place(x=80, y=70, height=25, width=250)

Sor_txt = Text(frame, font=("Times New Roman",15,"bold"), bg = "yellow", wrap=WORD)
Sor_txt.place(x=20, y=100, height=150, width=360)

list_txt = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value = list_txt)
comb_sor.place(x=20, y=255, height=30, width=110)
comb_sor.set("english")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=145, y=255, height=30, width=110)

comb_dest = ttk.Combobox(frame, value = list_txt)
comb_dest.place(x=270, y=255, height=30, width=110)
comb_dest.set("english")

dest_txt = Text(frame, font=("Times New Roman",15,"bold"), bg="yellow", wrap=WORD)
dest_txt.place(x=20, y=295, height=150, width=360)

root.mainloop()
