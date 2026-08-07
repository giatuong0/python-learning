from tkinter import *
import tkinter.messagebox
def save_data():
    try:
        fileD = open("giaohangnhanhsaves.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n"%depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n"%description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n"%address.get("1.0",END)) #Lenh luu dinh dang file saves cua khach%s la string #/n xuong dong` 1 at row 0 at collum to end get data
        depot.set("")
        description.delete(0, END)
        address.delete("1.0", END) #reset xoa cac o sau khi save

    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n%s" %ex)
    
def read_depots(file):
    depots=[]
    depots_f=open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots       #ham` doc cac lines cua file depot
    
app = Tk()
app.title('giaohangnhanh')
Label(app,text = "Depot:").pack()
depot= StringVar() # tao UI app muc depot se bang bien string o nut depot

options=read_depots("depots.txt")
OptionMenu(app, depot, *options).pack() # doc file cac dia chi trong depots.txt import all* vao UI optionmenu pack lai
      
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()# tao nut co entry hoac text field
      
Label(app, text = "Address").pack()
address=Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack() #su dung ham` save_data cho button save
app.mainloop() #loop cua app
