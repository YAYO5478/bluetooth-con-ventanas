import tkinter as tk
from tkinter import colorchooser
from tkinter import commondialog

# Crear la ventana principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Selector de Color")

        # Botón para abrir el selector de color
        self.boton_color = tk.Button(self, text="Elige un color", command=self.elegir_color)
        self.boton_color.pack(pady=20)

    def elegir_color(selfi):
        # Abrir el cuadro de diálogo de selección de color
        color = colorchooser.askcolor(title="Selecciona un color")
        
        # Verifica que el usuario haya seleccionado un color
        if color[1] is not None:
            # Cambia el fondo de la ventana principal al color elegido
            selfi.configure(bg=color[1])

# Iniciar la aplicación
app = App()
app.mainloop()
