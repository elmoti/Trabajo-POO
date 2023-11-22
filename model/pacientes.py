from datetime import date
from helper.validaciones import *


class Paciente:
    def __init__(self, ci: str, nombre: str, edad: int, sexo: str, fecha_nacimiento: date, direccion: str):
        self.__ci: str = valid_ci(ci)
        self.__nombre: str = valid_str("Nombre", nombre, 3, 100)
        self.__edad: int = valid_int("Edad", edad, 0, 150)
        self.__sexo: str = valid_sexo(sexo)
        self.__fecha_nacimiento: date = valid_date(
            "Fecha Nacimiento", fecha_nacimiento, date(date.today().year-150, 1, 1), date.today())
        self.__direccion: str = valid_str("Direccion", direccion, 10, 254)

    @property
    def ci(self) -> str:
        return self.__ci

    @ci.setter
    def ci(self, value: str) -> None:
        self.__ci = valid_ci(value)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self.__nombre = valid_str("Nombre", value, 3, 100)

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, value: int) -> None:
        self.__edad = valid_int("Edad", value, 0, 150)

    @property
    def sexo(self) -> str:
        return self.__sexo

    @sexo.setter
    def sexo(self, value: str) -> None:
        self.__sexo = valid_sexo(value)

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value: date) -> None:
        self.__fecha_nacimiento = valid_date(
            "Fecha Nacimiento", value, date(date.today().year-150, 1, 1), date.today())

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, value: str) -> None:
        self.__direccion = valid_str("Direccion", value, 10, 254)

    def __str__(self) -> str:
        paciente = "Paciente: {}, {}, {}, {}, {}, {}"
        return paciente.format(self.__ci, self.__nombre, self.__edad, self.__sexo,
                               self.fecha_nacimiento, self.direccion)
