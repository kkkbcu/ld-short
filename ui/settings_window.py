# settings_window.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.api_key_label = QLabel("API Key:")
        layout.addWidget(self.api_key_label)
        self.api_key_input = QLineEdit()
        layout.addWidget(self.api_key_input)

        self.secret_key_label = QLabel("Secret Key:")
        layout.addWidget(self.secret_key_label)
        self.secret_key_input = QLineEdit()
        layout.addWidget(self.secret_key_input)

        self.passphrase_label = QLabel("Passphrase:")
        layout.addWidget(self.passphrase_label)
        self.passphrase_input = QLineEdit()
        layout.addWidget(self.passphrase_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_settings(self):
        # 설정 저장 함수 (추후 구현)
        api_key = self.api_key_input.text()
        secret_key = self.secret_key_input.text()
        passphrase = self.passphrase_input.text()
        print(f"Settings saved: API Key={api_key}, Secret Key={secret_key}, Passphrase={passphrase}")
        self.close()
