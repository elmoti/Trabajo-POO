from ui.ui_acerca_de import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from helper.helper_functions import resource_path


class AcercaDe(QDialog, Ui_Dialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('images/hospital.svg')))
