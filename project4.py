from tkinter import Label, Tk 
import time
app = Tk()
app.title("🕛Digital Clock")
app.geometry("500x200")
app.resizable(False,False)
app.configure(bg="black")
clock_label=Label(app,bg="black",fg="cyan",font=("Helvetica", 40),
relief='flat')
clock_label.place(x=20 , y=20)
date_label = Label(app, bg="black", fg="lime", font=("Helvetica", 20), relief='flat')
date_label.place(x=20, y=90)

def update_time():
    current_date = time.strftime("%A, %d %B %Y")
    current_time = time.strftime("%I:%M:%S %p") 
    clock_label.config(text = current_time)
    date_label.config(text=current_date)
    clock_label.after(1000 , update_time)
update_time()
app.mainloop()