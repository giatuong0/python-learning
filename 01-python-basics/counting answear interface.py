from tkinter import* #import all * w no prefix from lib

def correct():
    num_good.set(num_good.get()+1)

def wrong():
    num_bad.set(num_bad.get()+1)

app=Tk()
app.title("TVN Game Show")
app.geometry('300x110+200+100')

num_good=IntVar()
num_good.set(0)
num_bad=IntVar()
num_bad.set(0)

lab=Label(app,text='When u are ready, click on the buttons!',height=3)
lab.pack()

lab1=Label(app,textvariable=num_good)
lab1.pack(side='left')

lab2=Label(app,textvariable=num_bad)
lab2.pack(side='right')

b1=Button(app,text="correct!", width=10,command=correct)
b1.pack(side='left', padx=10, pady=10)

b2=Button(app,text="Wrong!", width=10,command=wrong)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()
