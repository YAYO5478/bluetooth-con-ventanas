from tkinter import Tk, Canvas,Button   
from PIL import Image, ImageTk

# Crear ventana principal
root = Tk()
root.geometry("500x400")  # Ajusta el tamaño según tu imagen
root.title("bluetooth")

def mifuncion():
    print("mi botoon")


#crear el boton
boton=Button(root,text="+",command=mifuncion)
# Cargar la imagen de fondo
image = Image.open("imagen\Imagen inicio.png")  # Cambia la ruta por la de tu imagen
bg_image = ImageTk.PhotoImage(image)

# Crear un Canvas y agregar la imagen
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Agrega otros widgets encima si quieres
# Ejemplo: canvas.create_text para texto sobre la imagen
canvas.create_text(250, 200, text="Texto de ejemplo", fill="white", font=("Arial", 20))

root.mainloop()
