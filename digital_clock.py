from tkinter import Tk, Label
import time

app_window=Tk()
app_window.title("Digital Clock")
app_window.geometry(450*150)
app_window.resizable(1,1)

text_font=("Boulder",70,'Bold')
foreground="#1234r"
background="#67987"
border_width=28

label = Label(app_window,font=text_font,fg=foreground,bg=background,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock())

digital_clock()
app_window.mainloop()