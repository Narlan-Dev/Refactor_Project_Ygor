from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from styles.style import card_style, title_layout_style
from views.main_view.main_window import MainWindow

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Círculo de Mohr')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: white;")
        self.main_window = None
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)
        
        # Create card
        card = QWidget()
        card.setFixedSize(500, 500)
        card.setStyleSheet(card_style)
        
        # Card layout
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40)

        # Title section
        title_layout = QHBoxLayout()
        icon_label = QLabel()
        pixmap = QPixmap("icons/logo.png")
        icon_label.setPixmap(pixmap.scaled(90, 90, Qt.KeepAspectRatio))

        title_label = QLabel("Círculo de Mohr")
        title_label.setFont(QFont('Inter', 52, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(title_layout_style)

        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)
        title_layout.setAlignment(Qt.AlignCenter)

        # Form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(30)
        form_layout.setFormAlignment(Qt.AlignCenter)

        self.sigma_x_input = QLineEdit()
        self.sigma_x_input.setPlaceholderText("MPa")
        self.sigma_x_input.setFixedWidth(250)
        form_layout.addRow(QLabel("Tensão σx"), self.sigma_x_input)

        self.sigma_y_input = QLineEdit()
        self.sigma_y_input.setPlaceholderText("MPa")
        self.sigma_y_input.setFixedWidth(250)
        form_layout.addRow(QLabel("Tensão σy"), self.sigma_y_input)

        self.txy_input = QLineEdit()
        self.txy_input.setPlaceholderText("MPa")
        self.txy_input.setFixedWidth(250)
        form_layout.addRow(QLabel("Tensão τxy"), self.txy_input)

        # Submit button
        self.submit_button = QPushButton("SUBMETER")
        self.submit_button.setFixedHeight(50)
        self.submit_button.setFixedWidth(200)
        self.submit_button.clicked.connect(self.openNextScreen)

        # Add widgets to card layout
        card_layout.addLayout(title_layout)
        card_layout.addLayout(form_layout)
        card_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        # Add card to main layout
        main_layout.addWidget(card, alignment=Qt.AlignCenter)

    def validate_inputs(self):
        """Validate the input values"""
        try:
            sigma_x = float(self.sigma_x_input.text())
            sigma_y = float(self.sigma_y_input.text())
            txy = float(self.txy_input.text())
            return True
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 
                              'Please enter valid numerical values for all fields.')
            return False

    def openNextScreen(self):
        """Open the MainWindow with the input values"""
        if self.validate_inputs():
            sigma_x = self.sigma_x_input.text()
            sigma_y = self.sigma_y_input.text()
            txy = self.txy_input.text()

            # Create and show MainWindow
            self.main_window = MainWindow(sigma_x, sigma_y, txy, self)
            self.main_window.show()
            self.hide()
