import datetime
import os

class GestorCopiasSeguridad:
    def __init__(self, directorio_destino="copias_seguridad"):
        self.directorio_destino = directorio_destino

        # Crear el directorio de copias de seguridad si no existe
        if not os.path.exists(self.directorio_destino):
            os.makedirs(self.directorio_destino)

    def realizar_copia(self, dispositivo):
        # Generar el nombre del archivo de copia de seguridad
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"{dispositivo.nombre}_{fecha_actual}.cfg"

        # Realizar la copia de seguridad
        contenido_copia = f"Configuración de {dispositivo.nombre} ({dispositivo.direccion_ip})"

        # Guardar la copia de seguridad en un archivo
        ruta_archivo = os.path.join(self.directorio_destino, nombre_archivo)
        with open(ruta_archivo, "w") as archivo:
            archivo.write(contenido_copia)

        return f"Copia de seguridad guardada en {ruta_archivo}"