from tkinter import *

win = Tk()
win.geometry("500x424")
win.resizable(0, 0)
win.title("NOOBS CALCULATOR")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()
input_frame = Frame(win, width=51, height=60, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=3)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('timesnewroman', 22, 'bold'), textvariable=input_text, width=26, bg="white", bd=2, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = Frame(win, width=312, height=272.5, bg="silver")
btns_frame.pack()
 
clear = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "C", fg = "white", width = 33, height = 3, bd = 2, bg = "orange", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "/", fg = "white", width = 20, height = 3, bd = 2, bg = "grey", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
seven = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "7", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "8", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "9", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "*", fg = "white", width = 20, height = 3, bd = 2, bg = "grey", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

four = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "4", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "5", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "6", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "-", fg = "white", width = 20, height = 3, bd = 2, bg = "grey", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
one = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "1", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "2", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "3", fg = "red", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "+", fg = "white", width = 20, height = 3, bd = 2, bg = "grey", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "0", fg = "red", width = 21, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = ".", fg = "black", width = 10, height = 3, bd = 2, bg = "cyan", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, font=('timesnewroman', 10, 'bold'), text = "=", fg = "white", width = 20, height = 3, bd = 2, bg = "grey", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

win.mainloop()