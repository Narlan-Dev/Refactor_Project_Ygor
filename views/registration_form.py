from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFrame
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from styles.style import main_window_style, card_style
from views.show_info import ShowInfos

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set HD resolution window size
        self.setWindowTitle("Register Form")
        self.setFixedSize(1280, 720)

        # Main layout to center the card
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(main_window_style)
        self.initUI(main_layout)

    def initUI(self, main_layout):
        # Create a card (frame) to hold the form
        card = QFrame(self)
        card.setFixedSize(400, 550)
        card.setStyleSheet(card_style)

        # Layout for the form inside the card
        layout = QVBoxLayout(card)

        # Title and blue dot
        title_layout = QHBoxLayout()

        # Blue dot
        self.dot = QLabel(self)
        self.dot.setStyleSheet("background-color: #00bfff; border-radius: 8px; width: 16px; height: 16px;")
        self.dot.setFixedSize(16, 16)

        # Title label
        title_label = QLabel("Register")
        title_label.setObjectName("title")
        title_label.setFont(QFont("Arial", 28, QFont.Bold))

        # Add title and dot to layout
        title_layout.addWidget(self.dot)
        title_layout.addWidget(title_label)
        title_layout.setAlignment(Qt.AlignLeft)

        # Message label
        message_label = QLabel("Signup now and get full access to our app.")
        message_label.setObjectName("message")
        message_label.setAlignment(Qt.AlignCenter)

        # Input fields
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Firstname")

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Lastname")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")

        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setPlaceholderText("Confirm Password")

        # Grid layout for first name and last name
        name_layout = QGridLayout()
        name_layout.addWidget(self.first_name, 0, 0)
        name_layout.addWidget(self.last_name, 0, 1)

        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.openNextScreen)

        # Sign in message
        signin_label = QLabel('Already have an account? <a href="#">Signin</a>')
        signin_label.setObjectName("signin")
        signin_label.setAlignment(Qt.AlignCenter)

        # Add widgets to the card layout
        layout.addLayout(title_layout)
        layout.addWidget(message_label)
        layout.addLayout(name_layout)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.confirm_password)
        layout.addWidget(submit_button)
        layout.addWidget(signin_label)

        # Add the card to the center of the main layout
        main_layout.addWidget(card)

        # Timer to create a glowing pulse effect on the dot
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.pulseEffect)
        self.timer.start(500)

    def pulseEffect(self):
        # Toggle between two styles to mimic the glow effect
        if self.dot.styleSheet().find("scale(1.0)") != -1:
            self.dot.setStyleSheet("""
                background-color: #00bfff;
                border-radius: 8px;
                width: 16px;
                height: 16px;
                transform: scale(1.5);
                opacity: 0.7;
            """)
        else:
            self.dot.setStyleSheet("""
                background-color: #00bfff;
                border-radius: 8px;
                width: 16px;
                height: 16px;
                transform: scale(1.0);
                opacity: 1;
            """)

    def openNextScreen(self):
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        email = self.email.text()
        password = self.password.text()

        # Pass the current window (self) as the parent
        self.second_window = ShowInfos(first_name, last_name, email, password, self)
        self.second_window.show()
        self.hide()
