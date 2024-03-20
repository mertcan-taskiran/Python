import sys
from PyQt5 import QtWidgets, QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5")
    pencere.setGeometry(100,100,500,500)

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Merhaba Dünya!")
    etiket1.move(200,30)

    buton = QtWidgets.QPushButton(pencere) # Buton oluşturma
    buton.setText("Buton") # Buton içeriği
    buton.move(200,80) # Buton konumlandırma

    pencere.show()
    sys.exit(app.exec_())

Pencere()