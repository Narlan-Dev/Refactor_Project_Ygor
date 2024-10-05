from PyQt5.QtWidgets import QLabel
from .base_screen import BaseScreen

# FirstScreen with specific UI
class FirstScreen(BaseScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button.setText("Go to Screen 2")

    def handle_button_click(self):
        # Prepare data to pass to the second screen
        data_to_pass = "Hello from First Screen!"
        print(f"Passing data: {data_to_pass}")
        
        # Access the MainWindow and its screens directly
        main_window = self.parent()
        if main_window:
            main_window.screen2.receive_data(data_to_pass) 
            print("Data passed successfully.")
        else:
            print("Failed to access MainWindow.")

        # Switch to SecondScreen
        main_window.setCurrentIndex(1)

    def setup_specific_ui(self, layout):
        """Setup specific UI elements for FirstScreen"""
        specific_label = QLabel("This is First Screen")
        layout.addWidget(specific_label)
