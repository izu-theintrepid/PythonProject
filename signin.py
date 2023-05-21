from tkinter import *
from tkinter import messagebox

#roots
root=Tk()
root.title("AllVIT")
root.state('zoomed')
subg=PhotoImage(file="sign up bg.png")
subgl=Label(root,image=subg)
subgl.place(x=0,y=0)

#login func
def login():
    username="sammm"
    password="plswork"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame=Frame(bg='#ffafcc')

#widgets
login_label=Label(
    frame, text="Login", bg='#ffafcc', fg="#a2d2ff", font=("Montserrat", 30))
username_label=Label(
    frame, text="Username", bg='#ffafcc', fg="#FFFFFF", font=("Montserrat", 16))
username_entry=Entry(frame, font=("Arial", 16))
password_entry=Entry(frame, show="*", font=("Arial", 16))
password_label=Label(
    frame, text="Password", bg='#ffafcc', fg="#FFFFFF", font=("Montserrat", 16))
login_button=Button(
    frame, text="Login", bg="#a2d2ff", fg="#FFFFFF", font=("Montserrat", 16), command=login)

#widgets place
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

root.mainloop()  #loop to keep program runnin