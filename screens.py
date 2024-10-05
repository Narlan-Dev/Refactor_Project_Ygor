import sys
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

# Define the interface (abstract base class) without QWidget
class ScreenInterface(ABC):
    
    @abstractmethod
    def setup_ui(self):
        """Setup the UI elements"""
        pass
    
    @abstractmethod
    def handle_button_click(self):
        """Handle button clicks"""
        pass

# BaseScreen only inherits from QWidget
class BaseScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = None
        self.common_label = None  # Common label for all screens
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

    @abstractmethod
    def setup_specific_ui(self, layout):
        """Screen-specific UI setup, to be implemented by child classes"""
        pass

    @abstractmethod
    def handle_button_click(self):
        """Handle button click events"""
        pass

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
        main_window = self.parent()  # This should be MainWindow
        if main_window:
            main_window.screen2.receive_data(data_to_pass)  # Call method to pass data
            print("Data passed successfully.")
        else:
            print("Failed to access MainWindow.")

        # Switch to SecondScreen
        main_window.setCurrentIndex(1)

    def setup_specific_ui(self, layout):
        """Setup specific UI elements for FirstScreen"""
        specific_label = QLabel("This is First Screen")
        layout.addWidget(specific_label)

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
        self.received_label = QLabel("")  # Label to display received data
        layout.addWidget(self.received_label)

    def receive_data(self, data):
        """Receive data from FirstScreen and display it"""
        print(f"Received data: {data}")
        self.received_label.setText(data)  # Update the label with received data

# MainWindow that manages the screens
class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Create two screens and add them to the stacked widget
        self.screen1 = FirstScreen(self)
        self.screen2 = SecondScreen(self)

        self.addWidget(self.screen1)
        self.addWidget(self.screen2)

        # Set the window title
        self.setWindowTitle("Screen Switching Example")
        self.resize(300, 200)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
