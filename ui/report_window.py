# report_window.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class ReportWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report")
        self.setGeometry(200, 200, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.report_label = QLabel("Report:")
        layout.addWidget(self.report_label)

        # 보고서 내용 표시 (추후 구현)
        self.report_content = QLabel("No data available.")
        layout.addWidget(self.report_content)

        self.setLayout(layout)
