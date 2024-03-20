import sys
from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5")
    pencere.setGeometry(100,100,500,500)

    
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    # Horizontal Layout
    # h_box = QtWidgets.QHBoxLayout() # horizontal layout oluşturur
    # h_box.addWidget(okay) # okay butonunu ekler
    # h_box.addWidget(cancel) # cancel butonunu ekler
    # h_box.addStretch() # Boşluk
    # pencere.setLayout(h_box) # Horizontal layoutu pencereye ekler

    # Vertical Layout
    # v_box = QtWidgets.QVBoxLayout() # Vertical layout oluşturur
    # v_box.addWidget(okay) # okay butonunu ekler
    # v_box.addWidget(cancel) # cancel butonunu ekler
    # v_box.addStretch() # Boşluk
    # pencere.setLayout(v_box) # Vertical layoutu pencereye ekler

    # Butonları sağ alta konumlandırma
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    pencere.setLayout(v_box)


    pencere.show()
    sys.exit(app.exec_())

Pencere()