from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QDate
from datetime import date
from model.hospital import *
from PyQt5.QtGui import QIcon
from ui.ui_gestionar_doctor import Ui_Form
from helper.helper_functions import resource_path


class CRUDDoctor(QWidget, Ui_Form):
    def __init__(self, hospital: Hospital):
        super(CRUDDoctor, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__hospital: Hospital = hospital
        self.__current: Doctor = None
        self.__tabla: QTableWidget = self.tabla_doctor
        self.btn_insertar.clicked.connect(
            self.insertar_doctor)
        self.btn_actualizar.clicked.connect(self.actualizar)
        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_cerrar.clicked.connect(self.close)
        self.__tabla.itemClicked.connect(self.llenar_formulario_x_tabla)
        self.__tabla.setColumnCount(7)
        self.__tabla.setHorizontalHeaderLabels(
            ['RP', 'Nombre', 'Edad', 'Sexo', 'Fecha Nacimiento', 'Especialidad', 'Residente'])
        self.__tabla.horizontalHeaderItem(
            1).setToolTip('registro profesional')
        self.__tabla.resizeColumnsToContents()

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def nombre(self) -> str:
        return self.dc_nombre.text().strip()

    @nombre.setter
    def nombre(self, nombre: str):
        self.dc_nombre.setText(nombre)

    @property
    def registro_profesional(self) -> str:
        return self.dc_registro_profesional.text().strip()

    @registro_profesional.setter
    def registro_profesional(self, registro_profesional: str):
        self.dc_registro_profesional.setText(registro_profesional)

    @property
    def edad(self) -> str:
        return self.dc_edad.value()

    @edad.setter
    def edad(self, edad):
        self.dc_edad.setValue(edad)

    @property
    def sexo(self):
        if self.rbtn_masculino.isChecked():
            sex = 'Masculino'
        else:
            sex = 'Femenino'
        return sex

    @sexo.setter
    def sexo(self, sexo):
        if sexo == "Masculino":
            self.rbtn_masculino.setChecked(True)
            self.rbtn_femenino.setChecked(False)
        else:
            self.rbtn_masculino.setChecked(False)
            self.rbtn_femenino.setChecked(True)

    @property
    def fecha_nacimiento(self) -> date:
        return self.dc_fecha_nacimiento.date().toPyDate()

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha: date):
        d = QDate(fecha.year, fecha.month, fecha.day)
        self.dc_fecha_nacimiento.setDate(d)

    @property
    def especialidad(self) -> str:
        return self.dc_especialidad.text().strip()

    @especialidad.setter
    def especialidad(self, especialidad):
        self.dc_especialidad.setText(especialidad)

    @property
    def residente(self) -> str:
        residente = False
        if self.dc_residente.isChecked():
            residente = True
        return residente

    @residente.setter
    def residente(self, residente) -> None:
        self.dc_residente.setChecked(residente)

    def cargar_datos(self):
        self.vaciar_tabla()
        for doctor in self.hospital.doctores:
            doctor: Doctor = doctor
            residente = "No"
            if doctor.residente:
                residente = "Si"
            i = self.__tabla.rowCount()
            self.__tabla.insertRow(i)
            self.agregar_elemento_tabla(
                i, 0, doctor.registro_profesional)
            self.agregar_elemento_tabla(i, 1, doctor.nombre)
            self.agregar_elemento_tabla(i, 2, str(doctor.edad))
            self.agregar_elemento_tabla(i, 3, doctor.sexo)
            self.agregar_elemento_tabla(
                i, 4, doctor.fecha_nacimiento.strftime('%d, %b %Y'))
            self.agregar_elemento_tabla(i, 5, doctor.especialidad)
            self.agregar_elemento_tabla(i, 6, residente)
        self.__tabla.resizeColumnsToContents()

    def actualizar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para actualizarlo")
            if self.registro_profesional == self.__current.registro_profesional:
                self.validar_controles(actualizar=True)
                dc = Doctor(self.registro_profesional, self.nombre, self.edad,
                            self.sexo, self.fecha_nacimiento, self.especialidad, self.residente)
                self.hospital.actualizar_doctor(self.__current, dc)
                self.__current == None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                raise Exception(
                    "No puede modificar el registro_profesional del doctor para actualizar sus datos")
        except Exception as e:
            self.mostrar_error(e.args[0])

    def insertar_doctor(self):
        try:
            self.validar_controles()
            dc = Doctor(
                registro_profesional=self.registro_profesional,
                nombre=self.nombre,
                edad=self.edad,
                sexo=self.sexo,
                fecha_nacimiento=self.fecha_nacimiento,
                especialidad=self.especialidad,
                residente=self.residente,
            )
            self.hospital.add_doctor(dc)
            self.cargar_datos()
            self.restablecer_controles()
        except Exception as e:
            self.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        ind = self.__tabla.currentRow()
        if ind != -1:
            registro_profesional = self.__tabla.item(
                ind, 0).text()
            doctor: Doctor = self.hospital.getDoctorByRegistro(
                registro_profesional)
            self.setControls(doctor)
            self.__current = doctor

    def vaciar_tabla(self):
        while self.__tabla.rowCount() > 0:
            self.__tabla.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto) -> None:
        self.__tabla.setItem(
            fila, columna, QTableWidgetItem(texto))

    def validar_controles(self, actualizar=False) -> None:
        msg = 'El atributo {} es obligatorio.'
        if len(self.registro_profesional) == 0:
            raise Exception(msg.format('Registro Profesional'))
        if self.hospital.inHospitalDoctor(self.registro_profesional) and not actualizar:
            raise Exception(
                'Ya existe el doctor en nuestro registro busquelo en la tabla y actualicelo')
        if len(self.nombre) == 0:
            raise Exception(msg.format('Nombre'))
        if len(self.especialidad) == 0:
            raise Exception(msg.format('Especialidad'))
        if self.edad < 0:
            raise Exception("La edad no puede ser negativa")

    def restablecer_controles(self):
        self.registro_profesional = ''
        self.nombre = ''
        self.edad = 0
        self.sexo = 'Masculino'
        self.fecha_nacimiento = date(2000, 1, 1)
        self.especialidad = ''
        self.residente = False

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def setControls(self, doctor: Doctor) -> None:
        self.registro_profesional = doctor.registro_profesional
        self.nombre = doctor.nombre
        self.edad = doctor.edad
        self.sexo = doctor.sexo
        self.fecha_nacimiento = doctor.fecha_nacimiento
        self.especialidad = doctor.especialidad
        self.residente = doctor.residente

    def eliminar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para eliminarlo")
            if self.hospital.remove_doctor(self.__current):
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
                raise Exception(
                    "No se pudo eliminar el doctor")
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass
