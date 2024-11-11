import bluetooth
import tkinter as tk
from tkinter import filedialog, messagebox

class BluetoothManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Bluetooth")
        
        # Botones para acciones
        tk.Button(root, text="Buscar Dispositivos", command=self.buscar_dispositivos).pack(pady=10)
        tk.Button(root, text="Enviar Archivo", command=self.enviar_archivo).pack(pady=10)
        
        # Área de texto para mostrar resultados
        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack(pady=10)

    def buscar_dispositivos(self):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, "Buscando dispositivos...\n")
        dispositivos = bluetooth.discover_devices(lookup_names=True)
        
        if dispositivos:
            for direccion, nombre in dispositivos:
                self.resultado.insert(tk.END, f"Nombre: {nombre}, Dirección MAC: {direccion}\n")
        else:
            self.resultado.insert(tk.END, "No se encontraron dispositivos.\n")
    
    def enviar_archivo(self):
        archivo = filedialog.askopenfilename(title="Seleccionar Archivo")
        if not archivo:
            return

        # Dirección MAC del dispositivo (reemplaza esto con la dirección del dispositivo deseado)
        direccion_mac = simpledialog.askstring("Dirección MAC", "Introduce la dirección MAC del dispositivo:")
        
        if direccion_mac:
            try:
                socket_bluetooth = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                socket_bluetooth.connect((direccion_mac, 1))  # Conexión en el puerto RFCOMM 1
                self.resultado.insert(tk.END, f"Conectado a {direccion_mac}\n")

                with open(archivo, "rb") as f:
                    datos = f.read(1024)
                    while datos:
                        socket_bluetooth.send(datos)
                        datos = f.read(1024)

                self.resultado.insert(tk.END, "Archivo enviado con éxito.\n")
                socket_bluetooth.close()
            except bluetooth.BluetoothError as e:
                self.resultado.insert(tk.END, f"Error en la conexión: {e}\n")

# Crear ventana principal
root = tk.Tk()
app = BluetoothManager(root)
root.mainloop()
