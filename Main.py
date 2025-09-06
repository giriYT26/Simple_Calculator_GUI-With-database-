from tkinter import *
from tkinter import messagebox
from MYSQL_CONNECTION import login_window
import mysql.connector as mc 

def open_calculator(con,cur):
    global calculator_con, calculator_cur
    calculator_con=con
    calculator_cur=cur
    global window, equation_text, equation_label
    window=Tk()
    window.title("CALCULATOR")
    window.geometry("500x500")
    equation_text=""
    equation_label=StringVar()
    window.bind("<Key>",key_pressed)
    #---------------------------------------------------
    label=Label(window,textvariable=equation_label,font=("consolas",20),bg="black",fg="white",width=35,height=3)
    label.pack()
    #---------------------------------------------------
    frame=Frame(window)
    frame.pack()
    buttons=[
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "0",".","=","/"
    ]
    row=0
    col=0
    for button in buttons:
        if button=="=":
            btn=Button(frame,text=button,height=3,width=12,font=35,command=equals)
        else:
            btn=Button(frame,text=button,height=3,width=12,font=35,command=lambda b=button: button_press(b))
        btn.grid(row=row,column=col)
        col+=1
        if col > 3:
            col=0
            row+=1
    # Clear Button
    clear_button= Button(window,text="CLEAR",height=3,width=12,font=35,command=clear)
    clear_button.pack()
    #search History Button
    search_history_Button= Button(window,text="HISTORY",height=3,width=12,font=35,command=search_history)
    search_history_Button.pack(pady=10)
    #-------------------------
    window.mainloop()
def clear():
    global equation_text
    equation_text=''
    equation_label.set(equation_text)
def button_press(num):
    global equation_text 
    equation_text+=str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text,equation_label
    try:
        total=eval(equation_text)
        equation_label.set(total)
        ex="insert into calculations(equation,result) values (%s,%s)"
        val=(equation_text,str(total))
        calculator_cur.execute(ex,val)
        calculator_con.commit()
        equation_text=str(total)
    except ZeroDivisionError:
        equation_label.set("Division by Zero Error")
        equation_text=""
    except SyntaxError :
        equation_label.set("Syntax Error")
        equation_text=""
def search_history():
    search_his_window=Toplevel(window)
    search_his_window.title("CALCULATION HISTORY")
    search_his_window.geometry("500x500")
    calculator_cur.execute("select*from calculations")
    records=calculator_cur.fetchall()
    # display record
    display_text=""
    for record in records:
        display_text+=f'Eqution:{record[1]} | Result:{record[2]}\n ' #id:{record[0]} |
    label=Label(search_his_window,text=display_text,font=("consolas", 12))
    label.pack(padx=20,pady=20)
    def clear_history():
        messagebox.showwarning("WARINIG","Are you sure \nThen click ok ")
        calculator_cur.execute("DELETE FROM calculations")
        calculator_con.commit()
        label.config(text="Cleared History")
    clear_hist_button=Button(search_his_window,text="Clear the history",height=4,width=15,font=35,command=clear_history)
    clear_hist_button.pack(pady=10)   
def key_pressed(event):
    key=event.char
    if key.isdigit() or key in ["+","-","*","/","."]:
        button_press(key)
    elif key=="\r":
        equals()
    elif key=='\x08':
        clear()
    elif key=="j":
        search_history()

#--------------------------------------------------------------------------------------------

if __name__=="__main__":
    login=login_window()
    if login.run_login():
        open_calculator(login.con,login.cur)