from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from styles.style import card_style, title_layout_style
from views.show_info import ShowInfos

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set HD resolution window size
        self.setWindowTitle('Círculo de Mohr')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: white;") 
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)
        
        # Create a card (frame) to hold the form
        card = QWidget()
        card.setFixedSize(500, 500)
        card.setStyleSheet(card_style)
        
        # Layout for the form inside the card
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40) 

        # Title and blue dot
        title_layout = QHBoxLayout()
        icon_label = QLabel()
        pixmap = QPixmap("icons/logo.png")
        icon_label.setPixmap(pixmap.scaled(90, 90, Qt.KeepAspectRatio))

        # Title label
        title_label = QLabel("Círculo de Mohr")
        title_label.setFont(QFont('Inter', 52, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)

        # Add title and dot to layout
        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)
        title_layout.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(title_layout_style)

        # Formulário dentro do card
        form_layout = QFormLayout()
        form_layout.setSpacing(30)  # Mais espaçamento entre os campos
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

        # Botão SUBMETER
        submit_button = QPushButton("SUBMETER")
        submit_button.setFixedHeight(50)
        submit_button.setFixedWidth(200)
        submit_button.clicked.connect(self.openNextScreen)
        
        # Adicionando os widgets no layout do card
        card_layout.addLayout(title_layout)
        card_layout.addLayout(form_layout, stretch=1)
        card_layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        # Aplicando o layout ao card
        card.setLayout(card_layout)

        # Centraliza o card no layout principal
        main_layout.addWidget(card, alignment=Qt.AlignCenter)

        # Define o layout principal da janela
        self.setLayout(main_layout)

    def openNextScreen(self):
        sigma_x_input = self.sigma_x_input.text()
        sigma_y_input = self.sigma_y_input.text()
        txy_input = self.txy_input.text()

        # Pass the current window (self) as the parent
        self.second_window = ShowInfos(sigma_x_input, sigma_y_input, txy_input, self)
        self.second_window.show()
        self.hide()
