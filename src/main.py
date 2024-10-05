import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QStackedWidget
from screens.first_screen import FirstScreen
from screens.second_screen import SecondScreen

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
