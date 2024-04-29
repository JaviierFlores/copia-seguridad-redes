class DispositivoRed:
    def __init__(self, nombre, direccion_ip, tipo):
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.tipo = tipo

    def realizar_copia_seguridad(self):
        # Lógica para realizar la copia de seguridad del dispositivo
        return f"Se ha realizado una copia de seguridad para {self.nombre} ({self.direccion_ip})"