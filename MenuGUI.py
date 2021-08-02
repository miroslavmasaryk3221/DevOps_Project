# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSound
import subprocess
import os

def Dpepost():
    subprocess.Popen([r"main.py"])
def IMS():
    subprocess.Popen([r"IMS_check.py"])
def Service_acc():
    subprocess.Popen([r"Service_acc_check.py"])

# initializing button sound
buttonsound = {
    'c': QSound("button-20.wav"),
              }
file = {
    'a': subprocess,
              }



class Worker(QRunnable):
    '''
    Worker thread for DPEPost
    '''

    @pyqtSlot()
    def run(self):

        os.system("main.pyw")


class Worker_IMS(QRunnable):
    '''
    Worker thread for IMS
    '''

    @pyqtSlot()
    def run(self):
        os.system("IMS_check.py")


class Worker_ACC(QRunnable):
    '''
    Worker thread for Accounts check
    '''

    @pyqtSlot()
    def run(self):
        os.system("Service_acc_check.py")


#main Windows function
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.threadpool = QThreadPool()
        self.setWindowTitle("Transfer Check/Service accounts check ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        self.movie = QMovie("./servers/giphy.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
    # method for widgets

    def UiComponents(self):
        label1 = QLabel(self)
        label1.setText("<font color=white>Check Application</font>")
        label1.setFont(QFont('Times', 30))
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setGeometry(150, 5, 350, 50)

        class HoverButton(QPushButton):
            mouseHover = pyqtSignal(bool)

            def __init__(self, parent=None):
                QPushButton.__init__(self, parent)
                self.setMouseTracking(True)

            def enterEvent(self, event):
                self.mouseHover.emit(True)
                buttonsound['c'].play()

        # creating push button
        button = HoverButton(self)
        button.setText('Deutsche_Post check')

        # setting geometry of the push button
        button.setGeometry(20, 50, 140, 50)

        # setting background color to push button when mouse hover over it

        button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                            "QPushButton::hover"
                             "{"
                             "background-color : magenta;"
                             "}"
                             )

        # creating push button
        button1 = HoverButton(self)
        button1.setText('IMS check')

        # setting geometry of the push button
        button1.setGeometry(20, 120, 140, 50)

        # setting background color to push button when mouse hover over it

        button1.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : magenta;"
                             "}"
                             )

        # creating push button
        button2 = HoverButton(self)
        button2.setText('Service account check')

        # setting geometry of the push button
        button2.setGeometry(450, 50, 140, 50)

        # setting background color to push button when mouse hover over it

        button2.setStyleSheet("QPushButton"
                              "{"
                              "background-color : gray;"
                              "}"
                              "QPushButton::hover"
                              "{"
                              "background-color : magenta;"
                              "}"
                              )

        button.clicked.connect(self.clickme)
        button1.clicked.connect(self.clickme1)
        button2.clicked.connect(self.clickme2)

    def clickme(self):
        worker = Worker()
        self.threadpool.start(worker)

    def clickme1(self):
        worker = Worker_IMS()
        self.threadpool.start(worker)

    def clickme2(self):
        worker = Worker_ACC()
        self.threadpool.start(worker)






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.resize(600, 400)
    window.show()

    sys.exit(app.exec_())
