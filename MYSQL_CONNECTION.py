import mysql.connector as mc
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os 
set_default_color_theme("blue")
class Mysql_login:
    def __init__(self,hostname,username,password):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.con=None
        self.cur=None
        self.Connect_to_server()
    def Connect_to_server(self):
        try:
            self.con=mc.connect(
                host=self.hostname,
                username=self.username,
                password=self.password
                )
            self.cur=self.con.cursor()
            self.cur.execute("CREATE DATABASE IF NOT EXISTS calculator1_db")
            self.cur.execute("USE calculator1_db")
            self.cur.execute("CREATE TABLE IF NOT EXISTS calculations(id int AUTO_INCREMENT primary key, equation varchar(225),result varchar(225))")
            messagebox.showinfo("Calculator",f"Connected to the {self.username} MYSQL Server")
            return True
        except mc.Error:
            messagebox.showerror("ERROR",f"Failed to connect {self.username} to the MYSQL Sever")
            return False
        except ValueError:
            messagebox.showerror("ERROR",f"The fields can't be Empty")
            return False
class login_window:
        def __init__(self):
            self.login_successful=False # Initialize login status
            self.con=None
            self.cur=None
        def run_login(self):
            self.login_window=CTk()
            self.login_window.title("Calculator")
            self.login_window.geometry("600x450")
            self.login_window._set_appearance_mode("dark")
            self.add_bg_img()
            self.login_form()
            self.login_window.mainloop()
            return self.login_successful # Retuning login status
        def add_bg_img(self):
            try:
                image_path=os.path.join(os.path.dirname(__file__),"background_img.jpeg")
                img=Image.open(image_path)
                self.background_image=ImageTk.PhotoImage(img)
                L1=CTkLabel(master=self.login_window,image=self.background_image)
                L1.pack()
                #Adding a frame to fit the user credential entry
                self.fram=CTkFrame(master=L1,width=320,height=360,corner_radius=0,fg_color="#707070",border_color="#707070")
                self.fram.place(relx=0.5,rely=0.5,anchor=CENTER)
            except Exception as err:
                messagebox.showerror("QUIZ MASTER",F"ERROR|{err}")
        def login_form(self):
            def showpassword():
                if self.password.cget("show")=="":
                    self.password.configure(show="*")
                else:
                    self.password.configure(show="")
            def connect():
                host=self.host.get()
                username=self.username.get()
                password=self.password.get()
                obj=Mysql_login(host,username,password)
                if obj.Connect_to_server():
                    self.login_successful= True
                    self.con=obj.con
                    self.cur=obj.cur
                    self.login_window.destroy()
                    
            def keypressed(event):
                key=event.char
                if key=="\r":
                    connect()
            self.login_window.bind("<Key>",keypressed)
            try:
                CTkLabel(master=self.fram,text=" MySQL Connection Setup",font=("Arial", 16,"bold"),text_color="white").place(x=50,y=46) #()"Arial", 16) or ("Prociono",20)
                self.host=CTkEntry(master=self.fram,placeholder_text="Enter the Host:",text_color="black",font=("Segoe UI", 12,"bold"),fg_color="white",corner_radius=30,width=220)
                self.host.place(x=40,y=100)
                self.username=CTkEntry(master=self.fram,placeholder_text="Enter the Username:",text_color="black",font=("Segoe UI", 12,"bold"),fg_color="white",corner_radius=30,width=220)
                self.username.place(x=40,y=145)
                self.check_var=StringVar(value="off")
                self.showpassword=CTkCheckBox(master=self.fram,text="Show Password",font=("Segoe UI", 12,"bold"),variable=self.check_var,onvalue="on",offvalue="off",width=150,command=showpassword)
                self.showpassword.place(x=190,y=225)
                self.password=CTkEntry(master=self.fram,placeholder_text="Enter you Password",text_color="black",font=("Segoe UI", 12,"bold"),fg_color="white",corner_radius=30,width=220,show="*")
                self.password.place(x=40,y=185)
                self.submit=CTkButton(master=self.fram,text="LOGIN",text_color="black",font=("Arial", 16,"bold"),corner_radius=30,command=connect)
                self.submit.place(x=80,y=270)
            except Exception as err:
                messagebox.showerror("Calculator","ERROR|{err}")

"""""
if __name__=="__main__":
    login=login_window()
    if login.run_login():
        pass
"""""
# log_win=login_window()