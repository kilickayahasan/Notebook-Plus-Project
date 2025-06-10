import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp, QMainWindow

class Pencere (QWidget) :

    def __init__(self):

        super().__init__()

        self.init_ui ()

    def init_ui (self) :

        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)

        self.temizle.clicked.connect(self.ekrani_temizle)

        self.setLayout(v_box)

    def ekrani_temizle(self):

        self.yazi_alani.clear()


class Menu (QMainWindow) :

    def __init__(self):

        super().__init__()

        self.pencere = Pencere()
        self.setCentralWidget (self.pencere)   ## yazı alanını ana pencereye yerleştirdik

        menubar = self.menuBar ()

        dosya = menubar.addMenu ("Dosya")
        düzenle = menubar.addMenu ("Düzenle")

        dosya_ac = QAction ("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction ("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction ("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction (dosya_ac)
        dosya.addAction (dosya_kaydet)
        dosya.addAction (cikis)

        kes = QAction ("Kes",self)
        kes.setShortcut("Ctrl+X")

        kopyala = QAction ("Kopyala",self)
        kopyala.setShortcut("Ctrl+C")

        yapistir = QAction ("Yapıştır",self)
        yapistir.setShortcut("Ctrl+V")

        düzenle.addAction (kes)
        düzenle.addAction (kopyala)
        düzenle.addAction (yapistir)


        dosya_ac.triggered.connect (self.dosya_ac)
        dosya_kaydet.triggered.connect (self.dosya_kaydet)
        cikis.triggered.connect (self.cikis)

        kes.triggered.connect(self.pencere.yazi_alani.cut)
        kopyala.triggered.connect(self.pencere.yazi_alani.copy)
        yapistir.triggered.connect(self.pencere.yazi_alani.paste)


        self.setWindowTitle("Not Defteri")

        self.show()


    def dosya_ac (self) :

        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0] , "r",encoding = "utf-8") as file :

            self.pencere.yazi_alani.setText(file.read())

    def dosya_kaydet(self):

        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0] , "w", encoding="utf-8") as file :

            file.write(self.pencere.yazi_alani.toPlainText())

    def cikis(self):

        qApp.quit()



app = QApplication (sys.argv)

menu = Menu ()

sys.exit(app.exec_())





