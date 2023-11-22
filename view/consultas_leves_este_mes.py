from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget, QLineEdit
from PyQt5.QtGui import QIcon
from model.hospital import *
from ui.ui_consulta_leve_este_mes import Ui_Form
from helper.helper_functions import resource_path


class ConsultasLevesEsteMes(QWidget, Ui_Form):
    def __init__(self, hospital: Hospital):
        super(ConsultasLevesEsteMes, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__tabla: QTableWidget = self.tabla_consulta
        self.__tabla.setColumnCount(8)
        self.__tabla.setHorizontalHeaderLabels(
            ['Codigo', 'Doctor', 'Paciente', 'Fecha', 'Motivo', 'Diagnostico', 'Analisis', 'Tratamiento'])
        self.__tabla.resizeColumnsToContents()
        self.btn_accion.clicked.connect(self.cargar_datos)
        self.btn_cerrar.clicked.connect(self.close)
        self.__diagnostico: QLineEdit = self.cs_diagnostico

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def diagnostico(self) -> str:
        return self.__diagnostico.text().strip()

    @diagnostico.setter
    def diagnostico(self, value) -> None:
        self.__diagnostico.setText(value)

    def agregar_elemento_tabla(self, fila, columna, texto) -> None:
        self.__tabla.setItem(
            fila, columna, QTableWidgetItem(texto))

    def vaciar_tabla(self):
        while self.__tabla.rowCount() > 0:
            self.__tabla.removeRow(0)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def cargar_datos(self):
        self.vaciar_tabla()
        try:
            if len(self.diagnostico) > 0:
                listado: list[ConsultaLeve] = self.hospital.consultas_leves_este_mes_segun_diagnostico(
                    self.diagnostico)
                if len(listado) == 0:
                    raise Exception(
                        'No hay consultas leves a pacientes con ese diagnostico este mes')
                else:
                    for consulta in listado:
                        analisis = "No"
                        if consulta.analisis:
                            analisis = "Si"
                        i = self.__tabla.rowCount()
                        self.__tabla.insertRow(i)
                        self.agregar_elemento_tabla(
                            i, 0, consulta.codigo)
                        self.agregar_elemento_tabla(
                            i, 1, "{}-{}".format(consulta.doctor.nombre, consulta.doctor.registro_profesional))
                        self.agregar_elemento_tabla(
                            i, 2, "{}-{}".format(consulta.paciente.nombre, consulta.paciente.ci))
                        self.agregar_elemento_tabla(
                            i, 3, consulta.fecha.strftime('%d/%M/%Y'))
                        self.agregar_elemento_tabla(i, 4, consulta.motivo)
                        self.agregar_elemento_tabla(i, 5, consulta.diagnostico)
                        self.agregar_elemento_tabla(i, 6, analisis)
                        self.agregar_elemento_tabla(
                            i, 7, consulta.tratamiento.value)
                    self.__tabla.resizeColumnsToContents()
            else:
                raise Exception("Campo diagnostico requerido")
        except Exception as e:
            self.mostrar_error(e.args[0])
