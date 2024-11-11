import tkinter as tk

def on_click (event) :
    print ("Botón presionado")


ventana = tk. Tk ()
button = tk. Button(ventana, text="Haz clic aquí")
button. pack()
button. bind ("<Button-1>", on_click)
ventana. mainloop ()