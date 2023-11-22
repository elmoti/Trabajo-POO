from datetime import date
from model.pacientes import *
from model.doctor import *
from model.transporte import *
from model.tratamiento import *
from model.signo_vitales import *


class Consulta:
    def __init__(self, codigo: str, doctor: Doctor, paciente: Paciente, fecha: date, motivo: str) -> None:
        self.__codigo: str = codigo
        self.__doctor: Doctor = doctor
        self.__paciente: Paciente = paciente
        self.__fecha: date = fecha
        self.__motivo: str = motivo

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, value: str) -> None:
        self.__codigo = value

    @property
    def doctor(self) -> Doctor:
        return self.__doctor

    @doctor.setter
    def doctor(self, value: Doctor) -> None:
        self.__doctor = value

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, value: Paciente) -> None:
        self.__paciente = value

    @property
    def fecha(self) -> date:
        return self.__fecha

    @fecha.setter
    def fecha(self, value: date) -> None:
        self.__fecha = value

    @property
    def motivo(self) -> str:
        return self.__motivo

    @motivo.setter
    def motivo(self, value: str) -> None:
        self.__motivo = value

    def __str__(self):
        consulta = "Consulta: {}, {}, {}, {}, {}"
        p = repr(self.paciente)
        d = repr(self.doctor)
        return consulta.format(self.codigo, d, p, self.fecha,
                               self.motivo)


class ConsultaLeve(Consulta):
    def __init__(self, codigo: str, doctor: Doctor, paciente: Paciente, fecha: date, motivo: str,
                 diagnostico: str, analisis: bool, tratamiento: TRATAMIENTOS) -> None:
        super().__init__(codigo, doctor, paciente, fecha, motivo)
        self.__diagnostico: str = diagnostico
        self.__analisis: bool = analisis
        self.__tratamiento: TRATAMIENTOS = tratamiento

    @property
    def diagnostico(self) -> str:
        return self.__diagnostico

    @diagnostico.setter
    def diagnostico(self, value: str) -> None:
        self.__diagnostico = value

    @property
    def analisis(self) -> bool:
        return self.__analisis

    @analisis.setter
    def analisis(self, value: bool) -> None:
        self.__analisis = value

    @property
    def tratamiento(self) -> TRATAMIENTOS:
        return self.__tratamiento

    @tratamiento.setter
    def tratamiento(self, value: TRATAMIENTOS) -> None:
        self.__tratamiento = value


class ConsultaUrgencia(Consulta):
    def __init__(self, codigo: str, doctor: Doctor, paciente: Paciente, fecha: date, motivo: str,
                 sintoma_principal: str, signos_vitales: SignosVitales,
                 ingresado: bool, transporte: TRANSPORTE) -> None:
        super().__init__(codigo, doctor, paciente, fecha, motivo)
        self.__sintoma_principal: str = sintoma_principal
        self.__signos_vitales: SignosVitales = signos_vitales
        self.__ingresado: bool = ingresado
        self.__transporte: TRANSPORTE = transporte

    @property
    def sintoma_principal(self) -> str:
        return self.__sintoma_principal

    @sintoma_principal.setter
    def sintoma_principal(self, value: str) -> None:
        self.__sintoma_principal = value

    @property
    def signos_vitales(self) -> SignosVitales:
        return self.__signos_vitales

    @signos_vitales.setter
    def signos_vitales(self, value: SignosVitales) -> None:
        self.__signos_vitales = value

    @property
    def ingresado(self) -> bool:
        return self.__ingresado

    @ingresado.setter
    def ingresado(self, value: bool) -> None:
        self.__ingresado = value

    @property
    def transporte(self) -> TRANSPORTE:
        return self.__transporte

    @transporte.setter
    def transporte(self, value: TRANSPORTE) -> None:
        self.__transporte = value
