# Sanware Technologies - Tuyapy light control, written by Jack Franklin

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
root = tkinter.Tk()
from tuyapy import TuyaApi

from config import *

def convert(r,g,b):
    r = int(r)/255
    g = int(g)/255
    b = int(b)/255


    lowest = min(r,g,b)
    highest = max(r,g,b)


    l = round((lowest+highest)/2)
    s = int()
    h = int()

    if lowest == highest:
        s = 0

    else:
        if l >= 0.5:
            s = round(((highest-lowest)/(highest-lowest))/0.55)

    if highest == r:
        h = (g-b)/(highest-lowest)
    elif highest == g:
        h = 2.0+(b-r)/(highest-lowest)
    elif highest == b:
        h = 4.0+(r-g)/(highest-lowest)

    h = (h*60)

    if h < 0:
        h+=360


    return(h,100,50)



root.title("Tuyapy Light Control")
root.geometry("411x127")
root.resizable(False, False)
root.config(bg="white")

api = TuyaApi()
api.init(USERNAME, PASSWORD, COUNTRY_CODE)

def on():
    api.get_device_by_id(light_id).turn_on()

def off():
    api.get_device_by_id(light_id).turn_off()

def setColour():
    global colour
    rgb = colour.get().split(",")
    if colour.get() == "255,255,255":
        api.get_device_by_id(light_id).set_color_temp(10000)
    else:
        api.get_device_by_id(light_id).set_color(convert(rgb[0],rgb[1],rgb[2]))


ttk.Button(root,text="Turn light on",command=on,takefocus=False).pack()
ttk.Button(root,text="Turn light off",command=off,takefocus=False).pack()

colour = tkinter.Entry(root)
colour.pack()
ttk.Button(root,text="Set Colour",command=setColour,takefocus=False).pack()


tkinter.Label(root,text="Sanware Technologies",bg="white").pack()
root.mainloop()

Message #general
