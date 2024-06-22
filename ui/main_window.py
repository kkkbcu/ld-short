# main_window.py

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from settings_window import SettingsWindow
from strategy_settings_window import StrategySettingsWindow
from report_window import ReportWindow
form_class = uic.loadUiType("mainwindow.ui")[0]

class MainWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.trade_button.clicked.connect(self.start_trading)


        self.settings_button.clicked.connect(self.open_settings)
        self.strategy_button.clicked.connect(self.open_strategy_settings)
        self.report_button.clicked.connect(self.open_report)


    def start_trading(self):
        # 거래를 시작하는 함수 (추후 구현)
        self.status_label.setText("Current Status: Trading...")

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

    def open_strategy_settings(self):
        self.strategy_window = StrategySettingsWindow()
        self.strategy_window.show()

    def open_report(self):
        self.report_window = ReportWindow()
        self.report_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()