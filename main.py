import sys
from datetime import datetime, date
from PyQt5.QtWidgets import QApplication
from model.hospital import *
from view.inicio import Inicio


class Programa:
    def __init__(self) -> None:
        self.__hospital = Hospital()
        self.__view: Inicio = None

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def view(self) -> Inicio:
        return self.__view

    def load_data(self):
        p2 = Paciente("89031534223", "Angel", 33,
                      "Masculino", date(1989, 3, 15), "Calle CA #24")
        d1 = Doctor("69C", "Dayan Medrano", 50, "Masculino",
                    date(1970, 5, 31), "MGI", False)
        hoy = datetime.now()
        c1 = ConsultaLeve("CMGI-1", d1, p2, date(hoy.year, hoy.month, hoy.day),
                          "Dolor estomacal", "infección estomacal", True, TRATAMIENTOS.HIGIENICO_DIETETICO)
        self.hospital.add_paciente(p2)
        self.hospital.add_consulta(c1)
        sv1 = SignosVitales(38.5, 102, 90, 110)
        p3 = Paciente(ci="89051534223",
                      nombre="Pedro", edad=32, sexo="Masculino",
                      fecha_nacimiento=date(1990, 3, 15),
                      direccion="Calle CA #24")
        d2 = Doctor("89A", "Julia", 50, "Femenino",
                    date(1980, 5, 31), "MGI", False)
        hoy = datetime.now()
        c2 = ConsultaUrgencia("CMGI-2", d2, p3, date(hoy.year, hoy.month, hoy.day),
                              "Dolor estomacal", sintoma_principal="Dolor en el estomago",
                              ingresado=True,
                              transporte=TRANSPORTE.AMBULANCIA,
                              signos_vitales=sv1)
        self.hospital.add_paciente(p3)
        self.hospital.add_consulta(c2)
        self.hospital.add_doctor(d1)
        self.hospital.add_doctor(d2)

    def run(self):
        self.load_data()
        self.__view = Inicio(self.hospital)
        self.__view.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    programa = Programa()
    programa.run()
    app.exec()
