from PyQt5 import QtWidgets, uic,QtCore
import sys
from organizer import organizerFunctions

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Main.ui', self)
        self.btnOpen = self.findChild(QtWidgets.QPushButton,'btnSelectFolder')
        self.btnOpen.clicked.connect(self.btnOpenPressed)
        self.labelFolderPath = self.findChild(QtWidgets.QLabel, 'labelFolderName')
        self.textAreaLogs = self.findChild(QtWidgets.QTextBrowser, 'logArea')
        self.btnStartCleanUp = self.findChild(QtWidgets.QPushButton,'btnStartCleanUp')
        self.btnStartCleanUp.clicked.connect(self.btnStartCleanUpPressed)
        self.show()

    def btnOpenPressed(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", "")
        if fileName:
            self.fileName = QtCore.QDir.toNativeSeparators(fileName)
            self.labelFolderPath.setText(self.fileName)
            self.textAreaLogs.append("Selected " +self.fileName)

    def btnStartCleanUpPressed(self):
        if self.fileName:
            of = organizerFunctions(self.fileName)
            success = of.cleaner()
            self.textAreaLogs.append(of.getLogData())
            if success:
                self.textAreaLogs.append("Cleanup completed successfully!")
            else:
                self.textAreaLogs.append("Cleanup had errors! Try again later!!")
        else:
            self.textAreaLogs.append("Select a folder first!!")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
