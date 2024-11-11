# cliente_bluetooth.py
import bluetooth

# Dirección MAC del servidor (cambiar por la dirección del servidor)
direccion_servidor = "54:9F:40:30:F1"  # Reemplaza con la dirección MAC del servidor
puerto = 1  # Debe coincidir con el puerto que escucha el servidor

def enviar_archivo(nombre_archivo):
    # Crear el socket Bluetooth
    cliente = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    
    # Conectarse al servidor
    cliente.connect((direccion_servidor, puerto))
    print("Conectado al servidor Bluetooth.")
    
    # Enviar nombre del archivo
    cliente.send(nombre_archivo.encode())
    
    # Enviar archivo
    with open(nombre_archivo, "rb") as archivo:
        while True:
            datos = archivo.read(1024)
            if not datos:
                break
            cliente.send(datos)
    
    print(f"Archivo {nombre_archivo} enviado correctamente.")
    
    # Cerrar conexión
    cliente.close()

if __name__ == "__main__":
    # Nombre del archivo que deseas enviar
    nombre_archivo = "archivo_a_enviar.txt"
    enviar_archivo(nombre_archivo)
