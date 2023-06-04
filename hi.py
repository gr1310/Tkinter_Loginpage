import serial
import bluetooth
import sys
import tkinter as tk
import tkinter.font as font 

from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from tkinter import scrolledtext

main_window = tk.Tk()

main_window.title('Scan for nearby Bluetooth devices')

main_window.geometry("400x400")

text = tk.Text(main_window, height=30, width=30)
#text.grid(row=1, column=1, sticky=tk.EW)

def delete_s1():
    screen1.destroy()
    
def button_clicked1(): 
	global screen1
	screen1=Toplevel(main_window) 
	screen1.title("register")
    screen1.geometry("400x650")
    #print("Scanning") 
    Label(screen1,text="Scanning",width="400",height="3", font=("Times",16,"bold")).pack()
 
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    
    #print("Found {} devices.".format(len(nearby_devices)))
    Label(screen1,text="Found {} devices.".format(len(nearby_devices)),width="400",height="3", font=("Times",16,"bold")).pack()

    for addr, name in nearby_devices:
        #print("  {} - {}".format(addr, name))
        Label(screen1,text="  {} - {}".format(addr, name),width="400",height="3", font=("Times",16,"bold")).pack()
    #return 
    Label(screen1,text="").pack()
    Button(screen1,text="Close window",bg="#ffcccb",height=2, width= 20, command=delete_s1).pack()

Label(text="").pack()
Button(text="Scan Devices", height=1, width= 30, bg="#0077b6",font=("Times",13,"bold"), command=button_clicked1).pack()
    
Label(text="").pack()
Button(text='Exit',command=lambda: main_window.quit())


main_window.mainloop()
