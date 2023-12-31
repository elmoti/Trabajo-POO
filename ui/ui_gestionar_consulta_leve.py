# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Angel\Documents\github\moti\ui\gestionar_consulta_leve.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 788)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.cs_diagnostico = QtWidgets.QLineEdit(self.widget)
        self.cs_diagnostico.setObjectName("cs_diagnostico")
        self.gridLayout.addWidget(self.cs_diagnostico, 6, 1, 1, 1)
        self.cs_doctor = QtWidgets.QComboBox(self.widget)
        self.cs_doctor.setObjectName("cs_doctor")
        self.gridLayout.addWidget(self.cs_doctor, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.cs_tratamiento = QtWidgets.QComboBox(self.widget)
        self.cs_tratamiento.setObjectName("cs_tratamiento")
        self.cs_tratamiento.addItem("")
        self.cs_tratamiento.addItem("")
        self.cs_tratamiento.addItem("")
        self.gridLayout.addWidget(self.cs_tratamiento, 7, 1, 1, 1)
        self.cs_codigo = QtWidgets.QLineEdit(self.widget)
        self.cs_codigo.setObjectName("cs_codigo")
        self.gridLayout.addWidget(self.cs_codigo, 0, 1, 1, 1)
        self.cs_paciente = QtWidgets.QComboBox(self.widget)
        self.cs_paciente.setObjectName("cs_paciente")
        self.gridLayout.addWidget(self.cs_paciente, 2, 1, 1, 1)
        self.cs_fecha = QtWidgets.QDateEdit(self.widget)
        self.cs_fecha.setObjectName("cs_fecha")
        self.gridLayout.addWidget(self.cs_fecha, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.cs_motivo = QtWidgets.QLineEdit(self.widget)
        self.cs_motivo.setObjectName("cs_motivo")
        self.gridLayout.addWidget(self.cs_motivo, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.cs_analisis = QtWidgets.QCheckBox(self.widget)
        self.cs_analisis.setText("")
        self.cs_analisis.setObjectName("cs_analisis")
        self.gridLayout.addWidget(self.cs_analisis, 8, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.tabla_consulta = QtWidgets.QTableWidget(Form)
        self.tabla_consulta.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_consulta.setObjectName("tabla_consulta")
        self.tabla_consulta.setColumnCount(0)
        self.tabla_consulta.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla_consulta)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_insertar = QtWidgets.QPushButton(self.widget_2)
        self.btn_insertar.setObjectName("btn_insertar")
        self.horizontalLayout.addWidget(self.btn_insertar)
        self.btn_actualizar = QtWidgets.QPushButton(self.widget_2)
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.horizontalLayout.addWidget(self.btn_actualizar)
        self.btn_eliminar = QtWidgets.QPushButton(self.widget_2)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.btn_cerrar = QtWidgets.QPushButton(self.widget_2)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout.addWidget(self.btn_cerrar)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cs_codigo, self.tabla_consulta)
        Form.setTabOrder(self.tabla_consulta, self.btn_insertar)
        Form.setTabOrder(self.btn_insertar, self.btn_actualizar)
        Form.setTabOrder(self.btn_actualizar, self.btn_eliminar)
        Form.setTabOrder(self.btn_eliminar, self.btn_cerrar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestionar Consulta Leve"))
        self.label.setText(_translate("Form", "Codigo"))
        self.label_3.setText(_translate("Form", "Paciente"))
        self.label_5.setText(_translate("Form", "Diagnostico"))
        self.label_4.setText(_translate("Form", "Fecha"))
        self.cs_tratamiento.setItemText(0, _translate("Form", "Higieno-Dietético"))
        self.cs_tratamiento.setItemText(1, _translate("Form", "Medicina Natural"))
        self.cs_tratamiento.setItemText(2, _translate("Form", "Tradicional y/o Farmacológico"))
        self.label_7.setText(_translate("Form", "Motivo"))
        self.label_2.setText(_translate("Form", "Doctor"))
        self.label_6.setText(_translate("Form", "Tratamiento"))
        self.label_8.setText(_translate("Form", "Realizar Analisis"))
        self.tabla_consulta.setSortingEnabled(True)
        self.btn_insertar.setText(_translate("Form", "Insertar"))
        self.btn_actualizar.setText(_translate("Form", "Actualizar"))
        self.btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.btn_cerrar.setText(_translate("Form", "Cerrar"))
