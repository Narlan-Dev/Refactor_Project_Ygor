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
        self.button.setText("Go to Screen 2")  # Customize button text

    def handle_button_click(self):
        self.parent().setCurrentIndex(1)

    def setup_specific_ui(self, layout):
        """Setup specific UI elements for FirstScreen"""
        specific_label = QLabel("This is First Screen")
        layout.addWidget(specific_label)

# SecondScreen with specific UI
class SecondScreen(BaseScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button.setText("Go to Screen 1")  # Customize button text

    def handle_button_click(self):
        self.parent().setCurrentIndex(0)

    def setup_specific_ui(self, layout):
        """Setup specific UI elements for SecondScreen"""
        specific_label = QLabel("This is Second Screen")
        layout.addWidget(specific_label)

# MainWindow that manages the screens
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Create two screens and add them to the stacked widget
        self.screen1 = FirstScreen(self.stacked_widget)
        self.screen2 = SecondScreen(self.stacked_widget)

        self.stacked_widget.addWidget(self.screen1)
        self.stacked_widget.addWidget(self.screen2)

        # Set the layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

