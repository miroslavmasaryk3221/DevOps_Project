# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSound
import re
import subprocess
from PyQt5.QtWidgets import QLabel


def restartGame(self):
    self.close()
    subprocess.call("python" + "Service_acc_check.py", shell=True)


with open('accounts.txt') as my_file:
    acc_check = my_file.readlines()
i = 1
for i in range(15):
    acc_check[i] = re.sub("[^a-zA-Z0-9,-.@]+", "", acc_check[i], flags=re.IGNORECASE)

    i = i + 1

    if i == 14:
        break

# initializing button sound
buttonsound = {
    'c': QSound("button-20.wav"),
              }
# main Windows function


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Account check ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        self.movie = QMovie("./servers/Accounts_background.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()

    def onRestart(self, checked):
        QApplication.exit(self.EXIT_CODE_REBOOT)

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    # method for widgets

    def UiComponents(self):

        def Accheck(self, name, xpos, ypos, num):

            num = QLabel(self)

            num.setText("<font color=white>" + name + "</font>")
            num.setFont(QFont('Times', 11))
            palette = QPalette()
            palette.setColor(QPalette.Window, Qt.blue)
            num.setPalette(palette)
            num.setGeometry(xpos, ypos, 350, 50)

        def Unlocked(self, xpos, ypos, num):
            num = QLabel(self)
            num.setText("<font color=green>Not Locked</font>")
            num.setFont(QFont('Times', 11))
            palette = QPalette()
            palette.setColor(QPalette.Window, Qt.blue)
            num.setPalette(palette)
            num.setGeometry(xpos, ypos, 350, 50)

        def locked(self, xpos, ypos, num):
            num = QLabel(self)

            num.setText("<font color=red>Locked out</font>")
            num.setFont(QFont('Times', 11))
            palette = QPalette()
            palette.setColor(QPalette.Window, Qt.blue)
            num.setPalette(palette)
            num.setGeometry(xpos, ypos, 350, 50)

# s-archivDB
        def Check(self):

            Accheck(self, name="s-archivDB", xpos=40, ypos=5, num="label2")

            if acc_check[1] == "False":
                Unlocked(self, xpos=120, ypos=5, num="label2")
            else:
                locked(self, xpos=120, ypos=5, num="label2")
# s-qlik
            Accheck(self, name="s-qlik", xpos=40, ypos=20, num="label3")

            if acc_check[3] == "False":
                Unlocked(self, xpos=120, ypos=20, num="label3")
            else:
                locked(self, xpos=120, ypos=20, num="label3")
# s-runDB
            Accheck(self, name="s-runDB", xpos=40, ypos=35, num="label4")

            if acc_check[5] == "False":
                Unlocked(self, xpos=120, ypos=35, num="label4")
            else:
                locked(self, xpos=120, ypos=35, num="label4")
# s-runAPP
            Accheck(self, name="s-runAPP", xpos=40, ypos=50, num="label4")

            if acc_check[7] == "False":
                Unlocked(self, xpos=120, ypos=50, num="label4")
            else:
                locked(self, xpos=120, ypos=50, num="label4")
# s-runsvc
            Accheck(self, name="s-runsvc", xpos=40, ypos=65, num="label4")

            if acc_check[9] == "False":
                Unlocked(self, xpos=120, ypos=65, num="label4")
            else:
                locked(self, xpos=120, ypos=65, num="label4")
# s-runcps
            Accheck(self, name="s-runcps", xpos=40, ypos=80, num="label4")

            if acc_check[11] == "False":
                Unlocked(self, xpos=120, ypos=80, num="label4")
            else:
                locked(self, xpos=120, ypos=80, num="label4")
# s-runacc
            Accheck(self, name="s-runacc", xpos=40, ypos=95, num="label4")

            if acc_check[13] == "False":
                Unlocked(self, xpos=120, ypos=95, num="label4")
            else:
                locked(self, xpos=120, ypos=95, num="label4")

        Check(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = Window()

    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())
