from datetime import date
from dateutil.relativedelta import relativedelta
from model.hospital import *


def get_edad(fecha_nacimiento: date) -> int:
    edad = date.today().year - fecha_nacimiento.year
    cumpleanios = fecha_nacimiento + relativedelta(years=edad)
    if cumpleanios > date.today():
        edad = edad - 1
    return edad


class Datos:
    def __init__(self) -> None:
        self.pacientes: tuple = (
            ("89031534223", "Angel Napoles", get_edad(date(1989, 3, 15)), "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            ("95031534223", "Oscar Fuentes", get_edad(date(1995, 3, 15)), "Masculino",
             date(1995, 3, 15), "Calle RC#13, Camaguey"),
            ("70031534223", "Lester Amador", get_edad(date(1970, 3, 15)), "Masculino",
             date(1810, 3, 15), "Calle DF#20, Camaguey"),
            ("890315342", "Angel Napoles", get_edad(date(1989, 3, 15)), "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            ("asdasdasdas", "Angel Napoles", get_edad(date(1989, 3, 15)), "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            (12312312312, "Angel Napoles", get_edad(date(1989, 3, 15)), "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            ("89031534223", 123, get_edad(date(1989, 3, 15)), "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            ("89031534223", "Angel Napoles", "asdasd", "Masculino",
             date(1989, 3, 15), "Calle CA#24, Camaguey"),
            ("89031534223", "Angel Napoles", get_edad(
                date(1989, 3, 15)), "Masculino", "asdasd", "Calle CA#24, Camaguey"),
            ("89031534223", "Angel Napoles", get_edad(
                date(1989, 3, 15)), "Masculino", date(1989, 3, 15), 123123),
            ("89031534223", "Angel Napoles", get_edad(
                date(1989, 3, 15)), 123, date(1989, 3, 15), 123123),
        )
        self.pacientes_respuestas = (
            ("Paciente: 89031534223, Angel Napoles, 33, Masculino, 1989-03-15, Calle CA#24, Camaguey"),
            ("Paciente: 95031534223, Oscar Fuentes, 27, Masculino, 1995-03-15, Calle RC#13, Camaguey"),
            ("Fecha Nacimiento: debe ser mayor que 1872-01-01"),
            ("El carnet de identidad debe tener 11 caracteres"),
            ("El carnet de identidad debe tener solo dígitos"),
            ("El carnet de identidad solo acepta caracteres de texto"),
            ("Nombre: solo acepta caracteres de texto"),
            ("Edad: solo acepta caracteres numericos enteros"),
            ("Fecha Nacimiento: debe ser una fecha valida"),
            ("Direccion: solo acepta caracteres de texto"),
            ("El sexo debe contener solo caracteres de texto")
        )
