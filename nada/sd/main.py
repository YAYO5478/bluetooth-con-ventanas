# servidor_bluetooth.py
import bluetooth

def iniciar_servidor():
    # Crear el socket Bluetooth
    servidor = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    
    # Configurar el puerto de escucha
    puerto = bluetooth.PORT_ANY
    servidor.bind(("", puerto))
    servidor.listen(1)
    
    # Nombre del servicio
    bluetooth.advertise_service(servidor, "ServidorBluetooth",
                                service_classes=[bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])
    
    print("Esperando conexiones Bluetooth...")
    
    # Aceptar la conexión entrante
    cliente, direccion = servidor.accept()
    print(f"Conectado con {direccion}")
    
    # Recibir nombre del archivo
    nombre_archivo = cliente.recv(1024).decode()
    print(f"Recibiendo archivo: {nombre_archivo}")
    
    # Guardar el archivo
    with open(nombre_archivo, "wb") as archivo:
        while True:
            datos = cliente.recv(1024)
            if not datos:
                break
            archivo.write(datos)
    
    print(f"Archivo {nombre_archivo} recibido correctamente.")
    
    # Cerrar conexiones
    cliente.close()
    servidor.close()

if __name__ == "__main__":
    iniciar_servidor()
