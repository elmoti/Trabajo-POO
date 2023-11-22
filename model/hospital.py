from datetime import datetime
from model.consulta import *


class Hospital:
    def __init__(self) -> None:
        self.__consultas: list[Consulta] = []
        self.__doctores: list[Doctor] = []
        self.__pacientes: list[Paciente] = []

    def add_consulta(self, consulta: Consulta) -> None:
        self.__consultas.append(consulta)

    def remove_consulta(self, consulta: Consulta) -> bool:
        try:
            self.__consultas.remove(consulta)
            return True
        except:
            return False

    @property
    def consultas(self) -> list[Consulta]:
        return self.__consultas

    @consultas.setter
    def consultas(self, value: list[Consulta]) -> None:
        self.__consultas = value

    def actualizar_consulta(self, consulta_old: Consulta, consulta_new: Consulta) -> None:
        for i in range(len(self.consultas)):
            if self.consultas[i].codigo == consulta_old.codigo:
                self.consultas[i] = consulta_new

    def add_doctor(self, doctor: Doctor) -> None:
        self.__doctores.append(doctor)

    def remove_doctor(self, doctor: Doctor) -> bool:
        try:
            self.__doctores.remove(doctor)
            return True
        except:
            return False

    @property
    def doctores(self) -> list[Doctor]:
        return self.__doctores

    @doctores.setter
    def doctores(self, value: list[Doctor]) -> None:
        self.__doctores = value

    def actualizar_doctor(self, doctor_old: Doctor, doctor_new: Doctor) -> None:
        for i in range(len(self.doctores)):
            if self.doctores[i].registro_profesional == doctor_old.registro_profesional:
                self.doctores[i] = doctor_new

    def add_paciente(self, paciente: Paciente) -> None:
        self.__pacientes.append(paciente)

    def remove_paciente(self, paciente: Paciente) -> bool:
        try:
            self.__pacientes.remove(paciente)
            return True
        except:
            return False

    @property
    def pacientes(self) -> list[Paciente]:
        return self.__pacientes

    @pacientes.setter
    def pacientes(self, value: list[Paciente]) -> None:
        self.__pacientes = value

    @property
    def consultas_leve(self) -> list[ConsultaLeve]:
        listado: list[ConsultaLeve] = []
        for consulta in self.__consultas:
            if isinstance(consulta, ConsultaLeve) and consulta not in listado:
                listado.append(consulta)
        return listado

    @property
    def consultas_urgencia(self) -> list[ConsultaUrgencia]:
        listado: list[ConsultaUrgencia] = []
        for consulta in self.__consultas:
            if isinstance(consulta, ConsultaUrgencia) and consulta not in listado:
                listado.append(consulta)
        return listado

    def actualizar_paciente(self, paciente_old: Paciente, paciente_new: Paciente) -> None:
        for i in range(len(self.pacientes)):
            if self.pacientes[i].ci == paciente_old.ci:
                self.pacientes[i] = paciente_new

    def inHospitalPaciente(self, ci):
        for paciente in self.pacientes:
            if isinstance(paciente, Paciente) and paciente.ci == ci:
                return True
        return False

    def inHospitalConsulta(self, codigo):
        for consulta in self.consultas:
            if consulta.codigo == codigo:
                return True
        return False

    def inHospitalDoctor(self, registro_profesional):
        for doctor in self.doctores:
            if doctor.registro_profesional == registro_profesional:
                return True
        return False

    def getDoctorByRegistro(self, registro_profesional) -> Doctor | None:
        for doctor in self.doctores:
            if doctor.registro_profesional == registro_profesional:
                return doctor
        return None

    def getPacienteByCI(self, ci) -> Paciente | None:
        for paciente in self.pacientes:
            if paciente.ci == ci:
                return paciente
        return None

    def getConsultaByCodigo(self, codigo) -> Consulta | None:
        for consulta in self.consultas:
            if consulta.codigo == codigo:
                return consulta
        return None

# Todas las consultas duran al menos 5 minutos para el interrogatorio del paciente.
#  Si le envían análisis se demora otros 5 minutos.(leve)
#  Indicando el tratamiento el médico se demora alrededor de 3 minutos.(leve)
#  Tomando los signos vitales se emplean 5 minutos más.(urgencia)
#  Si el paciente se queda ingresado, los formularios del ingreso toman alrededor de 10
# minutos para llenarlos.(urgencia)

    def tiempo_promedio_consulta_codigo(self, codigo: str) -> str:
        resultado = "No se encontro consulta con ese codigo en el hospital"
        consulta_codigo: Consulta = None
        for consulta in self.consultas:
            if consulta.codigo == codigo:
                consulta_codigo = consulta

        if consulta_codigo is not None:
            tiempo_promedio = 5
            if isinstance(consulta_codigo, ConsultaLeve):
                if consulta_codigo.analisis:
                    tiempo_promedio += 5
                if len(consulta_codigo.tratamiento.value):
                    tiempo_promedio += 3
            if isinstance(consulta_codigo, ConsultaUrgencia):
                if consulta_codigo.ingresado:
                    tiempo_promedio += 10
                sv: SignosVitales = consulta_codigo.signos_vitales
                if sv.temperatura > 0 and sv.pulso > 0 and sv.sanguínea_mínima > 0 and sv.sanguínea_máxima > 0:
                    tiempo_promedio += 5
            resultado = "El tiempo promedio de la consulta con codigo({}) es: {}".format(
                codigo, tiempo_promedio)
        return resultado

    def signos_vitales_fecha_ci(self, fecha: date, ci: str) -> str:
        resultado = "No se encontro una consulta en la fecha({}) con el paciente de urgencia con ci({})".format(
            fecha, ci)
        for consulta in self.consultas:
            if consulta.fecha == fecha and consulta.paciente.ci == ci and isinstance(consulta, ConsultaUrgencia):
                resultado = "Los signos vitales del paciente son: {}".format(
                    str(consulta.signos_vitales))
        return resultado

# # d) Implemente la funcionalidad para determinar qué por ciento de las consultas de urgencia
# # atendieron a pacientes con presión alta teniendo en cuenta que para que sea presión alta la
# # mínima tiene que ser mayor de 90 y/o la máxima mayor de 130.

    def porciento_cu_paciente_presion_alta(self) -> str:
        paciente_presion_alta = 0.0
        for consulta in self.consultas_urgencia:
            if consulta.signos_vitales.sanguínea_mínima > 90 and consulta.signos_vitales.sanguínea_máxima > 130:
                paciente_presion_alta += 1
        resultado = round(
            (paciente_presion_alta/len(self.consultas_urgencia) * 100), 2)
        return "El porciento de pacientes con presion alta de las consultas de urgencia es de: {}%".format(resultado)

    def paciente_leve_mayor_edad(self) -> str:
        resultado = "No hay pacientes con consultas leves en el sistema"
        paciente_mayor: Paciente = None
        if len(self.consultas_leve) > 0:
            for consulta in self.consultas_leve:
                if len(consulta.diagnostico) > 0:
                    if paciente_mayor is not None:
                        if paciente_mayor.edad < consulta.paciente.edad:
                            paciente_mayor = consulta.paciente
                    else:
                        paciente_mayor = consulta.paciente
            resultado = "El paciente leve de mayor edad es: {}".format(
                str(paciente_mayor))
        return resultado

    def consultas_leves_este_mes_segun_diagnostico(self, diagnostico) -> list[ConsultaLeve]:
        listado: list[ConsultaLeve] = []
        hoy = datetime.now()
        for consulta in self.consultas_leve:
            if consulta.fecha.year == hoy.year and consulta.fecha.month == hoy.month and consulta.diagnostico == diagnostico:
                listado.append(consulta)
        listado = sorted(listado, key=lambda x: x.fecha.day, reverse=False)
        return listado
