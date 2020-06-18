from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QFontDialog, QMessageBox
from Ui_mainwindow import Ui_MainWindow
import sys
import os


class Notepad(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Notepad, self).__init__()
        self.setupUi(self)

        self.filename = None

        self.setWindowTitle("untitled")

        # File
        self.actionNew.triggered.connect(self.actionNew_triggered)
        self.actionOpen.triggered.connect(self.actionOpen_triggered)
        self.actionSave.triggered.connect(self.actionSave_triggered)
        self.actionSave_As.triggered.connect(self.actionSave_As_triggered)
        self.actionExit.triggered.connect(self.actionSave_As_triggered)
        self.actionIncrease_Font.triggered.connect(self.actionIncrease_Font_triggered)
        self.actionDecrease_Font.triggered.connect(self.actionDecrease_Font_triggered)

        # Format
        self.actionFont.triggered.connect(self.actionFont_triggered)
        self.actionColor.triggered.connect(self.actionColor_triggered)

        # View

        # Help
        self.actionAbout.triggered.connect(self.actionAbout_triggered)


    def actionNew_triggered(self):
        self.filename = None
        self.textEdit.clear()

        self.setWindowTitle("untitled")

    def actionOpen_triggered(self):
        self.filename = QFileDialog.getOpenFileName(self, "Open file", os.getenv("./"))[0]
        with open(self.filename, "r") as f:
            self.textEdit.setPlainText(f.read())

        self.setWindowTitle(self.filename)

    def actionSave_triggered(self):
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, "Save file", os.getenv("./"))[0]

        with open(self.filename, "w") as f:
            f.write(self.textEdit.toPlainText())

    def actionSave_As_triggered(self):
        self.filename = QFileDialog.getSaveFileName(self, "Save file", os.getenv("./"))[0]

        with open(self.filename, "w") as f:
            f.write(self.textEdit.toPlainText())

        self.setWindowTitle(self.filename)

    def actionSave_As_triggered(self):
        sys.exit(0)

    def actionFont_triggered(self):
        font = QFontDialog.getFont()
        self.textEdit.setFont(font[1])

    def actionColor_triggered(self):
        txt = self.textEdit.toPlainText()
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)
        self.textEdit.setPlainText(txt)
        
    def actionIncrease_Font_triggered(self):
        pass

    def actionDecrease_Font_triggered(self):
        pass

    def actionAbout_triggered(self):
        st = '''
        <h3>Simple Text Editor</h3>
        
        <h4>Python (PySide2)</h4>

        <div>Author: Md El</div>
        <div>Date: 14/11/2019</div>
        '''
        QMessageBox.about(self, "About", st)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Notepad()
    win.show()
    sys.exit(app.exec_())