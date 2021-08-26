#!/usr/bin/env python3

import tkinter as tk
import random

HEIGHT = 700
WIDTH = 800

lst1 = []

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#7EC545")
canvas.pack()

def trans():
    lst1 = []

    frame = tk.Frame(root, bg="#2F4858")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Title
    Label_middle = tk.Label(root, text="Generador la Primitiva", font="Romand 15 bold italic", bg="#7EC545", fg="black")
    Label_middle.place(relx=0.5, rely=0.05, anchor='center')

    label = tk.Label(frame, text="Presiona el botton para generar numeros!", bg="#2F4858", fg="white")
    label.place(relx=0.3, rely=0.25)

    # Random Number Function
    def rndm():
        
        button.place(relx=0.35, rely=0.15)
        label.place(relx=0.3, rely=0.1)

        # Green frame for lottery spin
        frme = tk.Frame(frame, bg="#1A9A86")
        frme.place(relx=0.2, rely=0.25, relheight=0.2, relwidth=0.6)

        # White frame for lottery spin
        labl = tk.Label(frme)
        labl.place(relx=0.03, rely=0.1, relwidth=0.93, relheight=0.8)

        a = random.sample(range(1,49),6)
        lst1.append(a)

        new = tk.Label(labl, text=a, font="small")
        new.place(relx=0.01, rely=0.35, relwidth=1)

    def home():

        home_frame = tk.Frame(root, bg="#7EC545")
        home_frame.place(relwidth=1, relheight=1)

        title = tk.Label(root, text="Generador la Primitiva", font="Roman 20 bold italic", bg="#7EC545", fg="black")
        title.place(relx=0.34, rely=0.29)
        copy = tk.Label(text="Creador: Mateo Ortega \n © 2008 - 2021 Mateo Ortega", fg="black", bg="#7EC545")
        copy.place(relx=0.38, rely=0.9)

        btn = tk.Button(root, text="Continuar", bg="gold", bd=5, fg="black", command=trans)
        btn.place(relx=0.35, rely=0.4, relwidth=0.3)



    message = """ 
    El uso de este generador es para generar 6 números para la primitiva! 
    entre 1 y el 49. Cuando pulses el botón 
    verde que pone "Generar números"
    van a salir 6 números justo por debajo. 
    Rellena tu papel de la primitiva y espero que pilles algo!"""

    # Button for generating numbers
    button = tk.Button(frame, text="Generar Numeros", bg="gold", fg="black", bd=5, font="Romand 11 italic", command=rndm)
    button.place(relx=0.35, rely=0.3, relheight=0.06, relwidth=0.3)

    # Read More Function
    def ppup():

        # Green frame for lottery checker output
        lower_frame = tk.Frame(root, bg="#1A9A86", bd=10)
        lower_frame.place(relx=0.2, rely=0.57, relwidth=0.6, relheight=0.2)

        # White frame for lottery checker output
        lbl = tk.Label(lower_frame)
        lbl.place(relwidth=1, relheight=1)

        mateo = tk.Label(lbl, text=message)
        mateo.place(relx=0, rely=0.02, relwidth=1, relheight=0.9)


    # Read More button
    popup = tk.Button(text="Leer mas", bg="#00AB6F", fg="black", bd="5", font="Romand 11 italic", command=ppup)
    popup.place(relx=0.3, rely=0.49, relwidth=0.2, relheight=0.05)

    back = tk.Button(text="Volver al inicio", bg="#00AB6F", fg="black", bd="5", font="Romand 11 italic", command=home)
    back.place(relx=0.5, rely=0.49, relwidth=0.2, relheight=0.05)

        # TITLE
title = tk.Label(root, text="Generador la Primitiva", font="Roman 20 bold italic", bg="#7EC545", fg="black")
title.place(relx=0.34, rely=0.29)

# Copyright lol
copy = tk.Label(text="Creador: Mateo Ortega \n © 2008 - 2021 Mateo Ortega", fg="black", bg="#7EC545")
copy.place(relx=0.38, rely=0.9)

btn = tk.Button(root, text="Continuar", bg="gold", bd=5, fg="black", command=trans)
btn.place(relx=0.35, rely=0.4, relwidth=0.3)
root.mainloop()
