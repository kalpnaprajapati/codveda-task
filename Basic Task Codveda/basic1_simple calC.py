# Python graphics CALCULATOR
from tkinter import *
 
#store variable 
store = "" 
 
def enter(num): 
    global store
    store = store + str(num) 
    equation.set(store) 
 
def equalenter(): 
    try: 
        global store 
        total = str(eval(store)) 
        equation.set(total) 
        store = "" 
    except: 
        equation.set(" error ") 
        store = "" 
 
def erase(): 
    global store 
    store = "" 
    equation.set("") 
 
if __name__ == "__main__": 
    graphics = Tk()
    button_font = ("Iras Demi",24)
    button = Button(graphics, font=button_font)
    graphics.configure(background="gray60") 
    graphics.title("Calculator") 
    graphics.geometry("265x149") 
    equation = StringVar()
    store_win = Entry(graphics, textvariable=equation)
    store_win.grid(columnspan=10, ipadx=100)
 
    b1 = Button(graphics, text=' 1 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(1), height=1, width=5) 
    b1.grid(row=2, column=0) 
 
    b2 = Button(graphics, text=' 2 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(2), height=1, width=5) 
    b2.grid(row=2, column=1) 
 
    b3 = Button(graphics, text=' 3 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(3), height=1, width=5) 
    b3.grid(row=2, column=2) 
 
    b4 = Button(graphics, text=' 4 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(4), height=1, width=5) 
    b4.grid(row=3, column=0) 
 
    b5 = Button(graphics, text=' 5 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(5), height=1, width=5) 
    b5.grid(row=3, column=1) 
 
    b6 = Button(graphics, text=' 6 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(6), height=1, width=5) 
    b6.grid(row=3, column=2) 
 
    b5 = Button(graphics, text=' 7 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(7), height=1, width=5) 
    b5.grid(row=4, column=0) 
 
    b8 = Button(graphics, text=' 8 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(8), height=1, width=5) 
    b8.grid(row=4, column=1) 
 
    b9 = Button(graphics, text=' 9 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(9), height=1, width=5) 
    b9.grid(row=4, column=2) 
 
    b0 = Button(graphics, text=' 0 ', fg='azure1', bg='gray20', 
                    command=lambda: enter(0), height=1, width=5) 
    b0.grid(row=5, column=0) 
 
    add = Button(graphics, text=' + ', fg='azure1', bg='gray20', 
                command=lambda: enter("+"), height=1, width=5) 
    add.grid(row=2, column=3) 
 
    sub = Button(graphics, text=' - ', fg='azure1', bg='gray20', 
                command=lambda: enter("-"), height=1, width=5) 
    sub.grid(row=3, column=3) 
 
    mul = Button(graphics, text=' * ', fg='azure1', bg='gray20', 
                    command=lambda: enter("*"), height=1, width=5) 
    mul.grid(row=4, column=3) 
 
    div = Button(graphics, text=' / ', fg='azure1', bg='gray20', 
                    command=lambda: enter("/"), height=1, width=5) 
    div.grid(row=5, column=3) 
 
    eq = Button(graphics, text=' = ', fg='azure1', bg='gray20', 
                command=equalenter, height=1, width=5) 
    eq.grid(row=5, column=2) 
 
    erase = Button(graphics, text='erase', fg='azure1', bg='gray20', 
                command=erase, height=1, width=5) 
    erase.grid(row=5, column='1') 
 
    Dec= Button(graphics, text='.', fg='azure1', bg='gray20', 
                    command=lambda: enter('.'), height=1, width=5) 
    Dec.grid(row=6, column=0) 
 
    graphics.mainloop()
