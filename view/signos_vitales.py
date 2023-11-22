from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from model.hospital import *
from ui.ui_signos_vitales import Ui_Dialog
from helper.helper_functions import resource_path


class ViewSignosVitales(QDialog, Ui_Dialog):
    def __init__(self, hospital):
        super(ViewSignosVitales, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.btn_accion.clicked.connect(self.accion)
        self.btn_cancelar.clicked.connect(self.close)
        self.__fecha: QDateEdit = self.fecha_consulta
        self.__ci: QLineEdit = self.carnet_paciente

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def ci(self):
        return self.__ci.text().strip()

    @ci.setter
    def ci(self, value):
        self.__ci.setText(value)

    @property
    def fecha(self) -> date:
        return self.__fecha.date().toPyDate()

    @fecha.setter
    def fecha(self, fecha: date):
        d = QDate(fecha.year, fecha.month, fecha.day)
        self.__fecha.setDate(d)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        if len(self.ci) == 0:
            raise Exception(msg.format('Carnet de Identidad'))
        if len(self.ci) != 11:
            raise Exception('El carné de identidad debe tener 11 dígitos.')
        try:
            ci = int(self.ci)
        except:
            raise Exception('El carné de identidad debe tener solo digitos')

    def restablecer_controles(self):
        self.ci = ''
        self.fecha = date(2000, 1, 1)

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def accion(self):
        try:
            self.validar_controles()
            msg = self.hospital.signos_vitales_fecha_ci(
                fecha=self.fecha, ci=self.ci)
            self.mostrar_informacion("Respuesta:", msg)
            self.restablecer_controles
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass
