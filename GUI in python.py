import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow ,QLabel
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        
        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",10))
        label.setGeometry(0,0,250,100)
        label.setStyleSheet("color: black;"
                            "background-color: #9c168e;"
                            "font-style: italic;"
                            "text-decoration: underline;")

       # label.setAlignment(Qt.AlignTop) #Vertically top
       # label.setAlignment(Qt.AlignBottom) #Vertically bottom
        #label.setAlignment(Qt.AlignVCenter)  #Vertically center
        #label.setAlignment(Qt.AlignRight) #Horizontally right
        #label.setAlignment(Qt.AlignLeft) #Horizontally left
        #label.setAlignment(Qt.AlignHCenter)#Horizontally center

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center and top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center and Bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center
        label.setAlignment(Qt.AlignCenter) #Shortcut






def main():
    app = QApplication(sys.argv)
    window  = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()