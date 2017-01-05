from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "mainwindow.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_dose_button.clicked.connect(self.CalculateTax)
    
    def CalculateTax(self):
        dose = int(self.dose_box.toPlainText())
        dose = (self.dose_rate.value())
        total_dose = dose  + ((dose / 100) * dose)
        total_dose_string = str(total_dose)
        self.results_window.setText(total_dose_string)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())