'''
#Import tkinter
from tkinter import * #* means importing everything tkinter has

#gui interaction
window = Tk()#object name, which help interact with the gui window

#adding input
inp = Label(window,text = "Ahoy there")
window.title("Don't know")#adding basic madification
window.geometry('500x700')
window.config(bg = "blue")

frame1 = Frame(window, width=300,height=200,cursor='dot') #adding frames and cursor type
frame2 = Frame(window, width=300,height=200,cursor='dotbox')# can also add color through bg
button1 = Button(frame1,text= "Button 1",bg="blue")#adding buttons with its name and color
button2 = Button(frame2,text="Button 2",bg ="green")

frame1.pack(side=TOP)#assigning side
frame2.pack(side=BOTTOM)
button1.pack()#closing button
button2.pack()
inp.pack()

#mainloop
window.mainloop()#need to execute the task/program
'''
#Entry box
from tkinter import *
window=Tk()

window.title("simple")
window.geometry("500x700")

label1 =Label(window,text="Mail")#it gives the label
label2 =Label(window,text="Password")

e1= Entry(window,width=40,borderwidth=5)#entry is used for typing
e2= Entry(window,width=40,borderwidth=5)


label1.grid(row=0,column=1)#grid is used to determine the rows and column
label2.grid(row=1,column=1)
e1.grid(row=0,column=2)#closing is necessary for executing the programe
e2.grid(row=1,column=2)

mainloop()