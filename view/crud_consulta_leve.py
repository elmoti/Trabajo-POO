from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QComboBox, QTableWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from datetime import date
from model.hospital import *
from ui.ui_gestionar_consulta_leve import Ui_Form
from helper.helper_functions import resource_path


class CRUDConsultaLeve(QWidget, Ui_Form):
    def __init__(self, hospital: Hospital):
        super(CRUDConsultaLeve, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.__current: Consulta = None
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__tabla: QTableWidget = self.tabla_consulta
        self.__tabla.setColumnCount(8)
        self.__tabla.setHorizontalHeaderLabels(
            ['Codigo', 'Doctor', 'Paciente', 'Fecha', 'Motivo', 'Diagnostico', 'Analisis', 'Tratamiento'])
        self.__tabla.resizeColumnsToContents()
        self.__tabla.itemClicked.connect(self.llenar_formulario_x_tabla)
        self.btn_insertar.clicked.connect(self.insertar_consulta)
        self.btn_actualizar.clicked.connect(self.actualizar)
        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_cerrar.clicked.connect(self.close)

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def codigo(self) -> str:
        return self.cs_codigo.text().strip()

    @codigo.setter
    def codigo(self, codigo: str):
        self.cs_codigo.setText(codigo)

    @property
    def motivo(self) -> str:
        return self.cs_motivo.text().strip()

    @motivo.setter
    def motivo(self, motivo: str):
        self.cs_motivo.setText(motivo)

    @property
    def fecha(self) -> date:
        return self.cs_fecha.date().toPyDate()

    @fecha.setter
    def fecha(self, fecha: date):
        d = QDate(fecha.year, fecha.month, fecha.day)
        self.cs_fecha.setDate(d)

    @property
    def doctor(self) -> Doctor:
        d: QComboBox = self.cs_doctor
        return d.currentData()

    @doctor.setter
    def doctor(self, doctor: Doctor):
        d: QComboBox = self.cs_doctor
        index = d.findData(doctor)
        d.setCurrentIndex(index)

    @property
    def paciente(self) -> Paciente:
        d: QComboBox = self.cs_paciente
        return d.currentData()

    @paciente.setter
    def paciente(self, paciente: Paciente):
        d: QComboBox = self.cs_paciente
        index = d.findData(paciente)
        d.setCurrentIndex(index)

    def vaciar_comboBox(self):
        doctor: QComboBox = self.cs_doctor
        paciente: QComboBox = self.cs_paciente
        for i in range(doctor.count()):
            doctor.removeItem(0)
        for i in range(paciente.count()):
            paciente.removeItem(0)

    @property
    def diagnostico(self) -> str:
        return self.cs_diagnostico.text().strip()

    @diagnostico.setter
    def diagnostico(self, diagnostico):
        self.cs_diagnostico.setText(diagnostico)

    @property
    def analisis(self) -> str:
        analisis = False
        if self.cs_analisis.isChecked():
            analisis = True
        return analisis

    @analisis.setter
    def analisis(self, analisis) -> None:
        self.cs_analisis.setChecked(analisis)

    @property
    def tratamiento(self) -> TRATAMIENTOS:
        tratamiento_dict = {
            "Higieno-Dietético": TRATAMIENTOS.HIGIENICO_DIETETICO,
            "Medicina Natural": TRATAMIENTOS.MEDICINA_NATURAL,
            "Tradicional y/o Farmacológico": TRATAMIENTOS.TRADICIONAL_FARMACEUTICO,
        }
        return tratamiento_dict[self.cs_tratamiento.currentText()]

    @tratamiento.setter
    def tratamiento(self, tratamiento: TRATAMIENTOS) -> None:
        index = self.cs_tratamiento.findText(
            tratamiento.value, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.cs_tratamiento.setCurrentIndex(index)

    def vaciar_tabla(self):
        while self.__tabla.rowCount() > 0:
            self.__tabla.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto) -> None:
        self.__tabla.setItem(
            fila, columna, QTableWidgetItem(texto))

    def validar_controles(self, actualizar=False) -> None:
        msg = 'El atributo {} es obligatorio.'
        if len(self.codigo) == 0:
            raise Exception(msg.format('Codigo'))
        if len(self.motivo) == 0:
            raise Exception(msg.format('Motivo'))
        if len(self.hospital.doctores) == 0:
            raise Exception("Agregue Doctores para poder crear la consulta")
        if len(self.hospital.pacientes) == 0:
            raise Exception("Agregue Pacientes para poder crear la consulta")
        if self.hospital.inHospitalConsulta(self.codigo) and not actualizar:
            raise Exception(
                'Ya existe la consulta en nuestro registro con ese codigo busquela en la tabla y actualicela')
        if len(self.diagnostico) == 0:
            raise Exception(msg.format('Diagnostico'))

    def restablecer_controles(self):
        self.codigo = ''
        self.motivo = ''
        self.diagnostico = ''
        self.fecha = date(2000, 1, 1)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def cargar_datos(self):
        self.vaciar_tabla()
        self.vaciar_comboBox()
        for consulta in self.hospital.consultas_leve:
            consulta: ConsultaLeve = consulta
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
                i, 3, consulta.fecha.strftime('%d, %b %Y'))
            self.agregar_elemento_tabla(i, 4, consulta.motivo)
            self.agregar_elemento_tabla(i, 5, consulta.diagnostico)
            self.agregar_elemento_tabla(i, 6, analisis)
            self.agregar_elemento_tabla(i, 7, consulta.tratamiento.value)

        self.__tabla.resizeColumnsToContents()

        comboBox_doctor: QComboBox = self.cs_doctor
        for doctor in self.hospital.doctores:
            comboBox_doctor.addItem(
                "Dr.: {} - {} - {}".format(doctor.nombre, doctor.especialidad, doctor.registro_profesional), doctor)

        comboBox_paciente: QComboBox = self.cs_paciente
        for paciente in self.hospital.pacientes:
            comboBox_paciente.addItem(
                "Paciente: {} - {}".format(paciente.ci, paciente.nombre), paciente)

    def insertar_consulta(self):
        try:
            self.validar_controles()
            consulta = ConsultaLeve(self.codigo, self.doctor,
                                    self.paciente, self.fecha, self.motivo,
                                    self.diagnostico, self.analisis, self.tratamiento)
            self.hospital.add_consulta(consulta)
            self.cargar_datos()
            self.restablecer_controles()
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass

    def llenar_formulario_x_tabla(self):
        ind = self.__tabla.currentRow()
        if ind != -1:
            codigo = self.__tabla.item(
                ind, 0).text()
            consulta: ConsultaLeve = self.hospital.getConsultaByCodigo(codigo)
            self.setControls(consulta)
            self.__current = consulta

    def setControls(self, consulta: ConsultaLeve):
        self.codigo = consulta.codigo
        self.doctor = consulta.doctor
        self.paciente = consulta.paciente
        self.motivo = consulta.motivo
        self.fecha = consulta.fecha
        self.diagnostico = consulta.diagnostico
        self.analisis = consulta.analisis
        self.tratamiento = consulta.tratamiento

    def actualizar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para actualizarlo")
            if self.codigo == self.__current.codigo:
                self.validar_controles(actualizar=True)
                consulta = ConsultaLeve(self.codigo, self.doctor, self.paciente,
                                        self.fecha, self.motivo, self.diagnostico,
                                        self.analisis, self.tratamiento)
                self.hospital.actualizar_consulta(self.__current, consulta)
                self.__current == None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                raise Exception(
                    "No puede modificar el codigo de la consulta para actualizar sus datos")
        except Exception as e:
            self.mostrar_error(e.args[0])

    def eliminar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para eliminarlo")
            if self.hospital.remove_consulta(self.__current):
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
                raise Exception(
                    "No se pudo eliminar la consulta")
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass
