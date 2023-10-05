import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import pyqtgraph as pg
import pandas as pd
from pyqtgraph import PlotWidget

uiclass, baseclass = pg.Qt.loadUiType("main.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handle_events()

    def handle_events(self):
        # import signal to ch1
        self.import_signal_ch1.triggered.connect(self.get_signal_file)
        # import signal to ch2
        self.import_signal_ch2.triggered.connect(self.get_signal_file)
        #draw on play
        # self.actionPlay_Pause.triggered.connect(self.draw)
        # self.play_button_1.clicked.connect(self.draw)

    def get_signal_file(self):
        # get path of signal files only of types (xls, csv, txt)
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , "(*.xls);;(*.txt);;(*.csv);;(*.xlsx)")
        # check the type of signal file
        file_type = file_path.split('.')[-1]
        if file_type == 'xls':
            return self.load_xls(file_path)
        elif file_type == 'xlsx':
            return self.load_xlsx(file_path)
        elif file_type == 'csv':
            return self.load_csv(file_path)
        else:
            return self.load_txt(file_path)

    def load_xlsx(self, file_path):
        data = pd.read_excel(file_path, header=None)
        x = data.iloc[:, 0].values
        y = data.iloc[:, 1].values
        self.draw(x, y)

    def load_xls(self, file_path):
        pass
    def load_txt(self, file_path):
        data = pd.read_csv(file_path, sep=',')
        x = data.iloc[:, 0].values
        y = data.iloc[:, 1].values
        self.draw(x, y)

    def load_csv(self, file_path):
        pass


    def draw(self, x, y):
        self.pen = pg.mkPen(color=(255,0,0))
        self.x1 , self.y1 = x, y
        self.widget.plot(self.x1,self.y1, pen=self.pen)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()