from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent, QIcon
from model.hospital import *
from view.crud_doctor import CRUDDoctor
from view.crud_paciente import CRUDPaciente
from view.crud_consulta_leve import CRUDConsultaLeve
from view.crud_consulta_urgencia import CRUDConsultaUrgencia
from view.calcular_tiempo_promedio import CacularTiempoPromedio
from view.signos_vitales import ViewSignosVitales
from view.consultas_leves_este_mes import ConsultasLevesEsteMes
from view.acerca_de import AcercaDe
from ui.ui_ventana_principal import Ui_MainWindow
from helper.helper_functions import resource_path


class Inicio(QMainWindow, Ui_MainWindow):
    def __init__(self, hospital: Hospital):
        super(Inicio, self).__init__()
        self.setupUi(self)
        self.__hospital: Hospital = hospital
        self.__crud_doctor: CRUDDoctor = None
        self.__crud_paciente: CRUDPaciente = None
        self.__crud_consulta_urgencia: CRUDConsultaUrgencia = None
        self.__crud_consulta_leve: CRUDConsultaLeve = None
        self.__tiempo_promedio: CacularTiempoPromedio = None
        self.__signos_vitales: ViewSignosVitales = None
        self.__consulta_leve_este_mes: ConsultasLevesEsteMes = None
        self.__acerca_de: AcercaDe = None
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
        self.opc_salir.triggered.connect(self.close)
        self.actionDoctor.triggered.connect(self.show_doctor)
        self.actionPaciente.triggered.connect(self.show_paciente)
        self.actionConsultaLeve.triggered.connect(
            self.show_consulta_leve)
        self.actionConsultaUrgencia.triggered.connect(
            self.show_consulta_urgencia)
        self.actionCalcular_Tiempo_Promedio.triggered.connect(
            self.show_tiempo_promedio)
        self.actionSignos_Vitales_segun_fecha_Consulta_y_CI_Paciente.triggered.connect(
            self.show_signos_vitales)
        self.actionConsultas_Urgencia_con_Pacientes_con_Presion_Alta.triggered.connect(
            self.show_porciento)
        self.actionPaciente_de_Mayor_Edad_en_las_Consultas_Leves.triggered.connect(
            self.show_paciente_leve_mayor)
        self.actionConsulta_Leves_este_mes_segun_diagnostico.triggered.connect(
            self.show_consultas_leves_este_mes)
        self.opc_acerca.triggered.connect(self.show_acerca_de)

    @property
    def hospital(self):
        return self.__hospital

    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap(resource_path('images/background.jpg'))
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)

    def mostrar_informacion(self, titulo, msg):
        QMessageBox.information(self, titulo, msg)

    def show_doctor(self):
        self.__crud_doctor = CRUDDoctor(self.hospital)
        self.__crud_doctor.cargar_datos()
        self.__crud_doctor.show()

    def show_paciente(self):
        self.__crud_paciente = CRUDPaciente(self.hospital)
        self.__crud_paciente.cargar_datos()
        self.__crud_paciente.show()

    def show_consulta_urgencia(self):
        self.__crud_consulta_urgencia = CRUDConsultaUrgencia(self.hospital)
        self.__crud_consulta_urgencia.cargar_datos()
        self.__crud_consulta_urgencia.show()

    def show_consulta_leve(self):
        self.__crud_consulta_leve = CRUDConsultaLeve(self.hospital)
        self.__crud_consulta_leve.cargar_datos()
        self.__crud_consulta_leve.show()

    def show_tiempo_promedio(self):
        self.__tiempo_promedio = CacularTiempoPromedio(self.hospital)
        self.__tiempo_promedio.show()

    def show_signos_vitales(self):
        self.__signos_vitales = ViewSignosVitales(self.hospital)
        self.__signos_vitales.show()

    def show_porciento(self):
        msg = self.hospital.porciento_cu_paciente_presion_alta()
        self.mostrar_informacion("Respuesta:", msg)

    def show_paciente_leve_mayor(self):
        msg = self.hospital.paciente_leve_mayor_edad()
        self.mostrar_informacion("Respuesta:", msg)

    def show_consultas_leves_este_mes(self):
        self.__consulta_leve_este_mes = ConsultasLevesEsteMes(self.hospital)
        self.__consulta_leve_este_mes.show()

    def show_acerca_de(self):
        self.__acerca_de = AcercaDe()
        self.__acerca_de.show()
