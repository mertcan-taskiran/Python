import sys
from PyQt5 import QtWidgets

def Pencere(): # Fonksiyon tanımlayın

    app = QtWidgets.QApplication(sys.argv) # PyQt5 uygulamasını başlatın

    pencere = QtWidgets.QWidget() # Bir pencere oluşturun

    pencere.setWindowTitle("PyQt5") # Pencere başlığını ayarlayın

    pencere.show() # Pencereyi ekranda gösterin

    sys.exit(app.exec_()) # Uygulamayı çalıştırın ve çıkış yapılana kadar bekleyin

Pencere() # Pencere fonksiyonunu çağırarak uygulamayı başlatın
