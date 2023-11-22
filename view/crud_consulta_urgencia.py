from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QComboBox, QTableWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from datetime import date
from model.hospital import *
from ui.ui_gestionar_consulta_urgencia import Ui_Form
from helper.helper_functions import resource_path


class CRUDConsultaUrgencia(QWidget, Ui_Form):
    def __init__(self, hospital: Hospital):
        super(CRUDConsultaUrgencia, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.__current: Consulta = None
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__tabla: QTableWidget = self.tabla_consulta
        self.__tabla.setColumnCount(12)
        self.__tabla.setHorizontalHeaderLabels(
            ['Codigo', 'Doctor', 'Paciente', 'Fecha', 'Motivo', 'Sintoma', 'Ingresado', 'Transporte', 'Temperatura', 'Pulso', 'SMin', 'SMax'])
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
    def sintoma_principal(self) -> str:
        return self.cs_sintoma_principal.text().strip()

    @sintoma_principal.setter
    def sintoma_principal(self, sintoma_principal):
        self.cs_sintoma_principal.setText(sintoma_principal)

    @property
    def ingresado(self) -> str:
        ingresado = False
        if self.cs_ingresar.isChecked():
            ingresado = True
        return ingresado

    @ingresado.setter
    def ingresado(self, ingresado) -> None:
        self.cs_ingresar.setChecked(ingresado)

    @property
    def transporte(self) -> TRANSPORTE:
        transporte_dict = {
            "Ambulancia": TRANSPORTE.AMBULANCIA,
            "Transporte Privado": TRANSPORTE.TRANSPORTE_PRIVADO,
            "Transporte Público": TRANSPORTE.TRANSPORTE_PUBLICO,
        }
        return transporte_dict[self.cs_transporte.currentText()]

    @transporte.setter
    def transporte(self, transporte) -> str:
        index = self.cs_transporte.findText(
            transporte.value, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.cs_transporte.setCurrentIndex(index)

    @property
    def temperatura(self) -> float:
        return self.cs_temperatura.value()

    @temperatura.setter
    def temperatura(self, temperatura):
        self.cs_temperatura.setValue(temperatura)

    @property
    def sanguínea_mínima(self) -> float:
        return self.cs_smin.value()

    @sanguínea_mínima.setter
    def sanguínea_mínima(self, sanguínea_mínima):
        self.cs_smin.setValue(sanguínea_mínima)

    @property
    def sanguínea_máxima(self) -> float:
        return self.cs_smax.value()

    @sanguínea_máxima.setter
    def sanguínea_máxima(self, sanguínea_máxima):
        self.cs_smax.setValue(sanguínea_máxima)

    @property
    def pulso(self) -> int:
        return self.cs_pulso.value()

    @pulso.setter
    def pulso(self, pulso):
        self.cs_pulso.setValue(pulso)

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
        if len(self.sintoma_principal) == 0:
            raise Exception(msg.format('Sintoma Principal'))

    def restablecer_controles(self):
        self.codigo = ''
        self.motivo = ''
        self.sintoma_principal = ''
        self.pulso = 0
        self.temperatura = 0.0
        self.sanguínea_mínima = 0.0
        self.sanguínea_máxima = 0.0
        self.fecha = date(2000, 1, 1)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def cargar_datos(self):
        self.vaciar_tabla()
        self.vaciar_comboBox()
        for consulta in self.hospital.consultas_urgencia:
            consulta: ConsultaUrgencia = consulta
            ingresado = "No"
            if consulta.ingresado:
                ingresado = "Si"
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
            self.agregar_elemento_tabla(i, 5, consulta.sintoma_principal)
            self.agregar_elemento_tabla(i, 6, ingresado)
            self.agregar_elemento_tabla(i, 7, consulta.transporte.value)
            self.agregar_elemento_tabla(
                i, 8, str(consulta.signos_vitales.temperatura))
            self.agregar_elemento_tabla(
                i, 9, str(consulta.signos_vitales.pulso))
            self.agregar_elemento_tabla(
                i, 10, str(consulta.signos_vitales.sanguínea_mínima))
            self.agregar_elemento_tabla(
                i, 11, str(consulta.signos_vitales.sanguínea_máxima))

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
            sv = SignosVitales(self.temperatura, self.pulso,
                               self.sanguínea_mínima, self.sanguínea_máxima)
            consulta = ConsultaUrgencia(self.codigo, self.doctor,
                                        self.paciente, self.fecha, self.motivo,
                                        self.sintoma_principal, sv, self.ingresado, self.transporte)
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
            consulta: ConsultaUrgencia = self.hospital.getConsultaByCodigo(
                codigo)
            self.setControls(consulta)
            self.__current = consulta

    def setControls(self, consulta: ConsultaUrgencia):
        self.codigo = consulta.codigo
        self.doctor = consulta.doctor
        self.paciente = consulta.paciente
        self.motivo = consulta.motivo
        self.fecha = consulta.fecha
        self.sintoma_principal = consulta.sintoma_principal
        self.ingresado = consulta.ingresado
        self.transporte = consulta.transporte
        self.temperatura = consulta.signos_vitales.temperatura
        self.pulso = consulta.signos_vitales.pulso
        self.sanguínea_mínima = consulta.signos_vitales.sanguínea_mínima
        self.sanguínea_máxima = consulta.signos_vitales.sanguínea_máxima

    def actualizar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para actualizarlo")
            if self.codigo == self.__current.codigo:
                self.validar_controles(actualizar=True)
                sv = SignosVitales(self.temperatura, self.pulso,
                                   self.sanguínea_mínima, self.sanguínea_máxima)
                consulta = ConsultaUrgencia(self.codigo, self.doctor,
                                            self.paciente, self.fecha, self.motivo,
                                            self.sintoma_principal, sv, self.ingresado, self.transporte)
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
