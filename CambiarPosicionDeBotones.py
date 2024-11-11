import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

# Botón en la parte superior
boton1 = tk.Button(ventana, text="Botón Superior")
boton1.pack(side=tk.TOP, pady=5)

# Botón en la parte inferior
boton2 = tk.Button(ventana, text="Botón Inferior")
boton2.pack(side=tk.BOTTOM, pady=5)

# Botón en el centro
boton3 = tk.Button(ventana, text="Botón Centro")
boton3.pack(side=tk.TOP, pady=50)
 
ventana.mainloop()
