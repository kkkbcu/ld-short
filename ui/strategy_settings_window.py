# strategy_settings_window.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class StrategySettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strategy Settings")
        self.setGeometry(200, 200, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.short_window_label = QLabel("Short EMA Window:")
        layout.addWidget(self.short_window_label)
        self.short_window_input = QLineEdit()
        layout.addWidget(self.short_window_input)

        self.long_window_label = QLabel("Long EMA Window:")
        layout.addWidget(self.long_window_label)
        self.long_window_input = QLineEdit()
        layout.addWidget(self.long_window_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_settings(self):
        # 전략 설정 저장 함수 (추후 구현)
        short_window = self.short_window_input.text()
        long_window = self.long_window_input.text()
        print(f"Strategy settings saved: Short EMA Window={short_window}, Long EMA Window={long_window}")
        self.close()
