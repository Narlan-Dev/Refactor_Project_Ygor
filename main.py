import sys
from PyQt5.QtWidgets import QApplication
from views.registration_form import RegistrationForm

def main():
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
