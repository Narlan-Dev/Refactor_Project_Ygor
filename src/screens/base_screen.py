from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class BaseScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = None
        self.common_label = None
        self.setup_ui()

    def setup_ui(self):
        """Common UI setup method shared by both FirstScreen and SecondScreen"""
        layout = QVBoxLayout()

        # Add a common label, shared across both screens
        self.common_label = QLabel("This is a common label for all screens")
        layout.addWidget(self.common_label)

        # Create a button (child classes will modify its behavior)
        self.button = QPushButton()  
        self.button.clicked.connect(self.handle_button_click)
        layout.addWidget(self.button)

        # Call the screen-specific setup
        self.setup_specific_ui(layout)

        self.setLayout(layout)

    def setup_specific_ui(self, layout):
        """Screen-specific UI setup, to be implemented by child classes"""
        pass

    def handle_button_click(self):
        """Handle button click events"""
        pass
