import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5")
    pencere.setGeometry(100,100,500,500) # Pencere boyutu

    etiket1 = QtWidgets.QLabel(pencere) # Label oluşturma
    etiket1.setText("Burası bir yazıdır.") # Label içeriği
    etiket1.move(200,30) # Label konumlandırma

    pencere.show()
    sys.exit(app.exec_())

Pencere()