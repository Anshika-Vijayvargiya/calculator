from tkinter import *

root=Tk()

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root.geometry("400x680")
root.title("Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,background="grey")
b=Button(f,text="C",padx=5,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=15,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=5,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="**",padx=5,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,background="grey")
b=Button(f,text="1",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=6,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f1=Frame(root,background="grey")
b=Button(f1,text="4",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f1,text="5",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f1,text="6",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f1,text="-",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f1.pack()

f2=Frame(root,background="grey")
b=Button(f2,text="7",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f2,text="8",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f2,text="9",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f2,text="*",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
f2.pack()

f1=Frame(root,background="grey")
b=Button(f1,text="0",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f1,text="=",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f1,text=".",padx=10,pady=5, font="lucida 30 bold")
b.pack(side="left",padx=10,pady=10)
b.bind("<Button-1>",click)


f1.pack()


root.mainloop()