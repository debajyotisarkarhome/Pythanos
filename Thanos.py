import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
import math

ro=tk.Tk()
addr=""

ro.configure(bg="#000123")
ro.title("Thanos")
tk.Label(text="Pick the file you wanna snap                  ",font=("Helvetica",15),bg="#000123",fg="cyan").grid(row=1,column=1,padx =50, pady = 30)
a=tk.Label(text="",font=("Helvetica",15),bg="#000123",fg="cyan")
a.grid(row=2,column=1, padx=20, pady = 30)
ro.iconbitmap("brain.ico")





def bu():
    global addr
    global a
    filename = askopenfilename()
    a.configure(text=filename)
    addr=filename

    
def snup():
    global a
    if addr=="":
        a.configure(text="Please select file to snap")
    else:
        fil=open(addr,"r")
        da=fil.read()
        indat=list(da)
        lu=len(indat)/2
        for i in range(0,math.floor(lu)):
            ao=random.randint(0,len(indat)-1)
            indat.pop(ao)
        fil.close()
        fil1=open(addr,"w")
        me=""
        for j in indat:
            me=me+j

        
        fil1.write(me)
        fil1.close()
        a.configure(text="The file has been put to balance")
        


imgo = tk.PhotoImage(file = r".\images.png") 
img2 = imgo.subsample(4,4)




tk.Button(ro,text="SNAP !!",command=snup,font=("Helvetica",10,"bold"),image=img2).grid(row=3,column=1)





e1=tk.Button(ro,text="Browse",command=bu,font=("Helvetica",10,"bold"))
e1.grid(row=1,column=2, padx =50, pady = 30)



#img = tk.PhotoImage(file = r".\tha.png") 
#img1 = img.subsample(6,6)

#tk.Label(ro, image = img1,bg="#000123").grid(row = 1,column =5,columnspan = 2, rowspan = 2, padx =50, pady = 2)



tk.mainloop()


