from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

class SeanceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouvelle séance")
        self.setStyleSheet("""
            QDialog {
                background-color: white;
                color: black;
            }
            QLineEdit {
                background-color: white;
                color: black;
            }
            QLabel {
                color: black;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: black;
            }
        """)

        self.nom_input = QLineEdit()
        self.duree_input = QLineEdit()
        self.duree_input.setPlaceholderText("en minutes")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nom de la séance :"))
        layout.addWidget(self.nom_input)
        layout.addWidget(QLabel("Durée (minutes) :"))
        layout.addWidget(self.duree_input)

        buttons_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Annuler")
        buttons_layout.addWidget(ok_btn)
        buttons_layout.addWidget(cancel_btn)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

    def get_values(self):
        return self.nom_input.text(), self.duree_input.text()
