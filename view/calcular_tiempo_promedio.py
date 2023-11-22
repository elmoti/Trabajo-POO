from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from model.hospital import *
from ui.ui_tiempo_promedio import Ui_Dialog
from helper.helper_functions import resource_path


class CacularTiempoPromedio(QDialog, Ui_Dialog):
    def __init__(self, hospital):
        super(CacularTiempoPromedio, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__hospital: Hospital = hospital
        self.btn_accion.clicked.connect(self.accion)
        self.btn_cancelar.clicked.connect(self.close)
        self.__codigo: QLineEdit = self.a_codigo

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def codigo(self):
        return self.__codigo.text().strip()

    @codigo.setter
    def codigo(self, value):
        self.__codigo.setText(value)

    def validar_controles(self):
        if len(self.codigo) == 0:
            raise Exception('El atributo codigo es obligatorio.')

    def restablecer_controles(self):
        self.codigo = ''

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def accion(self):
        try:
            self.validar_controles()
            msg = self.hospital.tiempo_promedio_consulta_codigo(self.codigo)
            self.mostrar_informacion("Respuesta:", msg)
            self.restablecer_controles
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass
