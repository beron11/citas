from aplicacion import Aplicacion
from celular import Celular
from correo import Correo


class Notificacion:
    def __init__(self):
        self.correo = Correo()
        self.celular = Celular()
        self.aplicacion = Aplicacion()

    def enviar_notificacion(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def verificar_correo(self):
        print(f"Verificando correo {self.correo}")
