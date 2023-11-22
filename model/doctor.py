from datetime import date
from typing import *


class Doctor:
    def __init__(self, registro_profesional: str, nombre: str, edad: int, sexo: str,
                 fecha_nacimiento: date, especialidad: str, residente: bool) -> None:
        self.__registro_profesional: str = registro_profesional
        self.__nombre: str = nombre
        self.__edad: int = edad
        self.__sexo: str = sexo
        self.__fecha_nacimiento: str = fecha_nacimiento
        self.__especialidad: str = especialidad
        self.__residente: bool = residente

    @property
    def registro_profesional(self) -> str:
        return self.__registro_profesional

    @registro_profesional.setter
    def registro_profesional(self, value: str) -> None:
        self.__registro_profesional = value

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self.__nombre = value

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, value: int) -> None:
        self.__edad = value

    @property
    def sexo(self) -> str:
        return self.__sexo

    @sexo.setter
    def sexo(self, value: str) -> None:
        self.__sexo = value

    @property
    def fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value: str) -> None:
        self.__fecha_nacimiento = value

    @property
    def especialidad(self) -> str:
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, value: str) -> None:
        self.__especialidad = value

    @property
    def residente(self) -> bool:
        return self.__residente

    @residente.setter
    def residente(self, value: bool) -> None:
        self.__residente = value

    def __str__(self):
        doctor = "Doctor: {}, {}, {}, {}, {}, {}, {}"
        residente = "no es residente"
        if self.residente:
            residente = "es residente"

        return doctor.format(self.registro_profesional, self.nombre, self.edad, self.sexo,
                             self.fecha_nacimiento, self.especialidad, residente)
