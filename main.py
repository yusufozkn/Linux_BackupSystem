from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui.ui_Mainwindow import Ui_MainWindow
import sys, os, json, time
import shutil

           

class Main(QMainWindow):

    global target_file
    target_file  = "/home/yusuf/Masaüstü/proje1/yedeklemeKlasoru"###----linux icin degisecek

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ConnectSignals()
        self.timer = QTimer()
        self.second = 5
        self.i=0
            

    def ConnectSignals(self):
        self.ui.btnKonumSec.clicked.connect(self.KonumSecTiklandi)
        self.ui.btnKonumSec_2.clicked.connect(self.KonumSec2_tiklandi)
        self.ui.btnStart.clicked.connect(self.Baslat_tiklandi)
        self.ui.btnStart_2.clicked.connect(self.Durdur_tiklandi)
        self.ui.comboBox.currentIndexChanged.connect(self.on_selection)
        self.ui.lbl1.setStyleSheet("color: red")
        self.ui.lbl1_2.setStyleSheet("color: red")
        self.ui.lbl1_3.setStyleSheet("color: red")
        self.ui.lbl1_4.setStyleSheet("color: red")
    
    def on_selection(self):
        
        global selection
        selection = self.ui.comboBox.currentText()

        print(selection)  

        if selection=="5 saniye":
            print("5 saniyee")
            self.second = 5
        elif selection =="5 dakika":
            print("5 dakikaa")
            self.second = 300
        elif selection =="30 dakika":
            print("30 dakikaa")
            self.second = 1800
        elif selection =="1 saat":
            print("1 saatt")
            self.second = 3600
        elif selection =="4 saat":
            print("4 saatt")  
            self.second = 14400     
        elif selection =="12 saat":
            print("12 saatt") 
            self.second = 1
        elif selection =="1 gün":
            print("1 günn")
            self.second = 86400


    def KonumSecTiklandi(self):
        print("bana tiklandi")
        global source_file
        
        kayitSonuc, iki = QFileDialog.getOpenFileName(None, "Baslik")
        if not kayitSonuc:
            print("bir sey secilmedi")
            
            return
        else:
            self.ui.txtKonum.setText(kayitSonuc)
            if not kayitSonuc:
                source_file = "" 
            else:
                source_file = kayitSonuc
            print(source_file)
            return source_file
 

    def KonumSec2_tiklandi(self):
        print("bana tiklandi")
        
        sonuc = QFileDialog.getExistingDirectory(None, "Baslik")
        global target_file
        target_file  = ""
        if not sonuc:
            print("bir sey secilmedi")
            target_file  = "/home/yusuf/yedeklemeKlasoru"
            self.ui.txtKonum_2.setText(target_file)
            return
        else:
            self.ui.txtKonum_2.setText(sonuc)

            target_file  = sonuc
            print(target_file )
            return target_file 

    
    def copy(self):
        
        try:
            file_path = source_file
            file_name, file_ext = os.path.splitext(file_path)


            print(file_name) #dosyanın tam uzantısını yazdırma
            print(file_ext)  #dosyanın .uzantısını yazdırma
            file_base_name = os.path.basename(file_name).replace(file_ext, "")
            print(file_base_name) #kaydelicek dosyanın adı



            shutil.copy(source_file ,target_file)

            timestamp = time.gmtime(os.path.getmtime(file_path))
            new_name = file_base_name + time.strftime('_%Y_%m_%d_%H_%M_%S', timestamp) +  file_ext
            print(target_file)
            print(new_name)
            new_loc = target_file +'/'+file_base_name+ file_ext
            test = target_file +'/'+new_name
            
            print(new_loc)
            os.rename(new_loc , test)


        except NameError:
            print("Kayıt yapılacak dosya seçilmedi...")
            self.Durdur_tiklandi()
            self.ui.txtKonum.setText("LUTFEN GECERLI BIR DOSYA SECIN \t\t===>")

        except shutil.SameFileError:
            print("Dosya Güncel...")
            self.Durdur_tiklandi()

       
        else:
            print("dosya kopyalandı")   
            


    def Baslat_tiklandi(self):
        
        self.timer.start(1000*self.second)
        self.ui.lbl1.setStyleSheet("color: green")
        self.ui.lbl1_2.setStyleSheet("color: green")
        self.ui.lbl1_3.setStyleSheet("color: green")
        self.ui.lbl1_4.setStyleSheet("color: green")

        self.timer.timeout.connect(self.copy)
        print("yedekleme basladi")

    def Durdur_tiklandi(self):
        
        self.ui.lbl1.setStyleSheet("color: red")
        self.ui.lbl1_2.setStyleSheet("color: red")
        self.ui.lbl1_3.setStyleSheet("color: red")
        self.ui.lbl1_4.setStyleSheet("color: red")
        print("yedekleme durdu...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = Main()
    wind.show()
    sys.exit(app.exec())
