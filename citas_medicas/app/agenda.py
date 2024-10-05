class Agenda:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        # Verificar si ya existe una cita en la misma fecha y hora
        for c in self.citas:
            if c.fecha == cita.fecha and c.hora == cita.hora:
                raise ValueError("Ya existe una cita en esa fecha y hora.")
        self.citas.append(cita)

    def cancelar_cita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
            return True
        return False

    def mover_cita(self, cita, nueva_fecha, nueva_hora):
        if cita not in self.citas:
            raise ValueError("La cita no existe en la agenda.")
        
        # Verificar si la nueva fecha y hora están disponibles
        for c in self.citas:
            if c != cita and c.fecha == nueva_fecha and c.hora == nueva_hora:
                raise ValueError("Ya existe una cita en la nueva fecha y hora.")
        
        cita.fecha = nueva_fecha
        cita.hora = nueva_hora

    def buscar_citas_por_fecha(self, fecha):
        return [cita for cita in self.citas if cita.fecha == fecha]

    def buscar_citas_por_paciente(self, paciente):
        return [cita for cita in self.citas if cita.paciente == paciente]

    def listar_citas(self):
        return sorted(self.citas, key=lambda c: (c.fecha, c.hora))

    def hay_conflicto(self, fecha, hora):
        return any(cita.fecha == fecha and cita.hora == hora for cita in self.citas)

    def __str__(self):
        if not self.citas:
            return "No hay citas programadas."
        
        citas_ordenadas = self.listar_citas()
        return "\n".join([f"{cita.fecha} {cita.hora}: {cita.paciente.nombre} {cita.paciente.apellido}" for cita in citas_ordenadas])
