from abc import ABC, abstractmethod

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
