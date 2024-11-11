import bluetooth
import tkinter as tk
from tkinter import messagebox
import threading

class BluetoothPairingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solicitud de Emparejamiento Bluetooth")

        self.add_device_button = tk.Button(root, text="Buscar y Emparejar Dispositivos Bluetooth", command=self.search_devices)
        self.add_device_button.pack(pady=20)

    def search_devices(self):
        # Buscar dispositivos Bluetooth
        self.devices = bluetooth.discover_devices(duration=8, lookup_names=True)
        if not self.devices:
            messagebox.showinfo("Resultado", "No se encontraron dispositivos Bluetooth.")
            return

        # Crear botones para cada dispositivo encontrado
        for addr, name in self.devices:
            device_button = tk.Button(self.root, text=f"Emparejar con {name} ({addr})", command=lambda addr=addr: self.pair_device(addr))
            device_button.pack(pady=5)

    def pair_device(self, addr):
        # Hilo para manejar la solicitud de emparejamiento
        threading.Thread(target=self.attempt_pairing, args=(addr,)).start()

    def attempt_pairing(self, addr):
        # Intento de conexión para iniciar solicitud de emparejamiento
        try:
            # Crear un socket Bluetooth para conectar al dispositivo
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((addr, 1))  # Canal RFCOMM 1 (generalmente usado en dispositivos móviles)
            
            # Si la conexión es exitosa, muestra mensaje
            messagebox.showinfo("Emparejamiento", f"Emparejado exitosamente con {addr}.")
            socket.close()
        except bluetooth.btcommon.BluetoothError as e:
            # Si falla, mostrar mensaje de error y cancelar
            messagebox.showwarning("Error de Emparejamiento", f"No se pudo emparejar con {addr}. Error: {str(e)}")

# Crear y ejecutar la aplicación
root = tk.Tk()
app = BluetoothPairingApp(root)
root.mainloop()
