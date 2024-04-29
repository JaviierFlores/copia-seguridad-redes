from dispositivo import DispositivoRed
from gestor_copias import GestorCopiasSeguridad

# Configuración
directorio_destino = "copias_seguridad"

# Crear instancia del gestor de copias de seguridad
gestor_copias = GestorCopiasSeguridad(directorio_destino)

# Crear instancias de dispositivos de red
router = DispositivoRed("Router1", "192.168.1.1", "Router")
switch = DispositivoRed("Switch1", "192.168.1.2", "Switch")

# Realizar copias de seguridad de los dispositivos
print(gestor_copias.realizar_copia(router))
print(gestor_copias.realizar_copia(switch))
