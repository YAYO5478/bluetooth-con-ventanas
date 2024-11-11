from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
# Crear la ventana principal
root = Tk()
root.title("Botón en Canvas")
root.geometry("400x300")

# Crear un Canvas
canvas = Canvas(root, width=400, height=150, bg="lightgrey")
canvas.pack()

# Función para obtener la posición (x, y) del clic
def imprimir_ubicacion_mouse(x, y):
    print(f"Posición del mouse: X = {x}, Y = {y}")
    
#cargar imagen
image = Image.open("imagen\Imagen inicio.png")  # Cambia la ruta por la de tu imagen
bg_image = ImageTk.PhotoImage(image)

# Crear un Canvas y agregar la imagen
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Crear el botón y configurarlo en el Canvas
boton = Button(root, text="Haz clic aquí", command=lambda: print("Botón presionado"), 
               width=15, height=2)  # Modifica el tamaño con width y height
canvas.create_window(500, 400, window=boton)  # Posiciona el botón en el centro del canvas


# Configura el listener de movimiento del mouse


# Ejecutar la aplicación
root.mainloop()
