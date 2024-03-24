from tkinter import *
import tkinter as tk
INFO=tk.Tk() 
   
width= INFO.winfo_screenwidth() 
height= INFO.winfo_screenheight()
#setting tkinter window size
INFO.geometry("%dx%d" % (width, height))
INFO.title("RESUME")

def text():

    Label(INFO,width="300", text=" ", bg="orange",fg="white").pack()

    l = Label(text="KRISHAN MOHAN SINGH", width=40,
            height=5, font= ('Forte')).pack(pady=10, side= TOP, anchor="w")
    

text()

INFO.mainloop()
    