from PyQt5.QtWidgets import QLabel
from .base_screen import BaseScreen

# SecondScreen with specific UI
class SecondScreen(BaseScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button.setText("Go to Screen 1")

    def handle_button_click(self):
        self.parent().setCurrentIndex(0)

    def setup_specific_ui(self, layout):
        """Setup specific UI elements for SecondScreen"""
        specific_label = QLabel("This is Second Screen")
        layout.addWidget(specific_label)
        self.received_label = QLabel("") 
        layout.addWidget(self.received_label)

    def receive_data(self, data):
        """Receive data from FirstScreen and display it"""
        print(f"Received data: {data}")
        self.received_label.setText(data)  # Update the label with received data
