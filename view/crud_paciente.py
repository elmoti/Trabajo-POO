from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from datetime import date
from model.hospital import *
from ui.ui_gestionar_paciente import Ui_Form
from helper.helper_functions import resource_path


class CRUDPaciente(QWidget, Ui_Form):
    def __init__(self, hospital: Hospital):
        super(CRUDPaciente, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.__current: Paciente = None
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.__tabla: QTableWidget = self.paciente_tabla
        self.__tabla.itemClicked.connect(self.llenar_formulario_x_tabla)
        self.btn_insertar.clicked.connect(self.insertar_paciente)
        self.btn_actualizar.clicked.connect(self.actualizar)
        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_cerrar.clicked.connect(self.close)

        self.__tabla.setColumnCount(6)
        self.__tabla.setHorizontalHeaderLabels(
            ['CI', 'Nombre', 'Edad', 'Sexo', 'Fecha Nacimiento', 'Dirección'])
        self.__tabla.horizontalHeaderItem(
            1).setToolTip('Carné de Identidad')
        self.__tabla.resizeColumnsToContents()

    @property
    def hospital(self) -> Hospital:
        return self.__hospital

    @property
    def nombre(self) -> str:
        return self.paciente_nombre.text().strip()

    @nombre.setter
    def nombre(self, nombre: str):
        self.paciente_nombre.setText(nombre)

    @property
    def ci(self) -> str:
        return self.paciente_ci.text().strip()

    @ci.setter
    def ci(self, ci: str):
        self.paciente_ci.setText(ci)

    @property
    def edad(self) -> str:
        return self.paciente_edad.value()

    @edad.setter
    def edad(self, edad):
        self.paciente_edad.setValue(edad)

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
        return self.paciente_fecha_nacimiento.date().toPyDate()

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha: date):
        d = QDate(fecha.year, fecha.month, fecha.day)
        self.paciente_fecha_nacimiento.setDate(d)

    @property
    def direccion(self) -> str:
        return self.paciente_direccion.text().strip()

    @direccion.setter
    def direccion(self, direccion):
        self.paciente_direccion.setText(direccion)

    def vaciar_tabla(self):
        while self.__tabla.rowCount() > 0:
            self.__tabla.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto) -> None:
        self.__tabla.setItem(
            fila, columna, QTableWidgetItem(texto))

    def validar_controles(self, actualizar=False) -> None:
        msg = 'El atributo {} es obligatorio.'
        if len(self.ci) == 0:
            raise Exception(msg.format('Carnet de Identidad'))
        if len(self.nombre) == 0:
            raise Exception(msg.format('Nombre'))
        if len(self.ci) != 11:
            raise Exception('El carné de identidad debe tener 11 dígitos.')
        try:
            ci = int(self.ci)
        except:
            raise Exception('El carné de identidad debe tener solo digitos')
        if self.hospital.inHospitalPaciente(self.ci) and not actualizar:
            raise Exception(
                'Ya existe el paciente en nuestro registro busquelo en la tabla y actualicelo')
        if len(self.direccion) == 0:
            raise Exception(msg.format('Dirección'))
        if self.edad < 0:
            raise Exception("La edad no puede ser negativa")

    def restablecer_controles(self):
        self.ci = ''
        self.nombre = ''
        self.edad = 0
        self.sexo = 'Masculino'
        self.fecha_nacimiento = date(2000, 1, 1)
        self.direccion = ''

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def cargar_datos(self):
        self.vaciar_tabla()
        for paciente in self.hospital.pacientes:
            paciente: Paciente = paciente
            i = self.__tabla.rowCount()
            self.__tabla.insertRow(i)
            self.agregar_elemento_tabla(i, 0, paciente.ci)
            self.agregar_elemento_tabla(i, 1, paciente.nombre)
            self.agregar_elemento_tabla(i, 2, str(paciente.edad))
            self.agregar_elemento_tabla(i, 3, paciente.sexo)
            self.agregar_elemento_tabla(
                i, 4, paciente.fecha_nacimiento.strftime('%d, %b %Y'))
            self.agregar_elemento_tabla(i, 5, paciente.direccion)
        self.__tabla.resizeColumnsToContents()

    def insertar_paciente(self):
        try:
            # self.validar_controles()
            pl = Paciente(
                ci=self.ci,
                nombre=self.nombre,
                edad=self.edad,
                sexo=self.sexo,
                fecha_nacimiento=self.fecha_nacimiento,
                direccion=self.direccion,
            )
            self.hospital.add_paciente(pl)
            self.cargar_datos()
            self.restablecer_controles()
        except Exception as e:
            self.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        ind = self.__tabla.currentRow()
        if ind != -1:
            ci = self.__tabla.item(
                ind, 0).text()
            pl: Paciente = self.hospital.getPacienteByCI(ci)
            self.setControls(pl)
            self.__current = pl

    def setControls(self, pl: Paciente) -> None:
        self.ci = pl.ci
        self.nombre = pl.nombre
        self.edad = pl.edad
        self.sexo = pl.sexo
        self.fecha_nacimiento = pl.fecha_nacimiento
        self.direccion = pl.direccion

    def actualizar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para actualizarlo")
            if self.ci == self.__current.ci:
                # self.validar_controles(actualizar=True)
                pl = Paciente(self.ci, self.nombre, self.edad, self.sexo,
                              self.fecha_nacimiento, self.direccion)
                self.hospital.actualizar_paciente(self.__current, pl)
                self.__current == None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                raise Exception(
                    "No puede modificar el carnet de identidad del paciente leve para actualizar sus datos")
        except Exception as e:
            self.mostrar_error(e.args[0])

    def eliminar(self):
        try:
            if self.__current is None:
                raise Exception(
                    "Seleccione un elemento de la tabla para eliminarlo")
            if self.hospital.remove_paciente(self.__current):
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
            else:
                self.__current = None
                self.cargar_datos()
                self.restablecer_controles()
                raise Exception(
                    "No se pudo eliminar el paciente")
        except Exception as e:
            self.mostrar_error(e.args[0])
        pass
