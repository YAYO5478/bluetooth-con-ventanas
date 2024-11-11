import tkinter as tk
from tkinter import messagebox, Toplevel
import bluetooth
import threading

class BluetoothApp:
    def __init__(self, root, ancho=400, alto=300):
        self.root = root
        self.root.title("Gestión de Dispositivos Bluetooth")
        
        # Obtener el tamaño de la pantalla
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()
        
        # Calcular la posición x e y para centrar la ventana
        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2
        
        # Ajustar la posición y el tamaño de la ventana
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
        
        # Botón para abrir la ventana de búsqueda de dispositivos
        self.add_device_button = tk.Button(root, text="Agregar dispositivos Bluetooth", command=self.open_search_window)
        self.add_device_button.pack(pady=20)

    def open_search_window(self):
        # Crear una nueva ventana para buscar dispositivos
        self.search_window = Toplevel(self.root)
        self.search_window.title("Buscar Dispositivos Bluetooth")
        
        # Etiqueta y botón de búsqueda
        tk.Label(self.search_window, text="Buscando dispositivos...").pack(pady=10)
        
        # Ejecutar escaneo en un hilo separado
        threading.Thread(target=self.scan_for_devices).start()

    def scan_for_devices(self):
        # Escaneo de dispositivos Bluetooth cercanos
        nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8)
        
        # Mostrar dispositivos encontrados o mensaje de no encontrados
        if not nearby_devices:
            tk.Label(self.search_window, text="No se encontraron dispositivos Bluetooth.").pack()
        else:
            for addr, name in nearby_devices:
                device_button = tk.Button(
                    self.search_window, text=f"Conectar a {name} ({addr})",
                    command=lambda addr=addr: self.connect_to_device(addr)
                )
                device_button.pack(pady=5)

    def connect_to_device(self, addr):
        # Intento de conexión con el dispositivo con un temporizador de 20 segundos
        try:
            threading.Thread(target=self.attempt_connection, args=(addr,)).start()
        except bluetooth.BluetoothError:
            messagebox.showerror("Error", "No se pudo conectar con el dispositivo.")

    def attempt_connection(self, addr):
        try:
            # Crear socket Bluetooth
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.settimeout(20.0)  # Timeout de 20 segundos
            socket.connect((addr, 1))  # Conexión en el canal 1

            # Mostrar mensaje de éxito
            messagebox.showinfo("Conexión", f"Conectado exitosamente a {addr}")
            socket.close()
        except bluetooth.BluetoothError:
            messagebox.showwarning("Sin Respuesta", "No hubo respuesta. Volviendo a buscar dispositivos.")
            self.open_search_window()  # Regresar a la ventana de búsqueda
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def incoming_request(self, addr):
        # Simulación de solicitud de vinculación entrante
        response = messagebox.askyesno("Solicitud de Vinculación", f"¿Aceptar vinculación de {addr}?")
        if response:
            self.confirm_pairing(addr)  # Aceptar vinculación
        else:
            messagebox.showinfo("Rechazo", "La vinculación ha sido rechazada.")  # Rechazar vinculación

    def confirm_pairing(self, addr):
        # Confirmación de vinculación exitosa
        messagebox.showinfo("Vinculación", f"Vinculado exitosamente con {addr}.")

# Configuración de la ventana principal
root = tk.Tk()
ancho_ventana = 400
alto_ventana = 300
app = BluetoothApp(root, ancho=ancho_ventana, alto=alto_ventana)
root.mainloop()
