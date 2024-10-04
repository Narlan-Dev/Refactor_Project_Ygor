import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

def load_stylesheet(filename):
    with open(filename, 'r') as file:
        stylesheet = file.read()
    return stylesheet

def on_submit():
    user_input = textbox.text()
    label.setText(f"{user_input}")

app = QApplication(sys.argv)
app.setStyleSheet(load_stylesheet('style/model.qss'))

window = QWidget()
window.setWindowTitle('Testing Styles')
window.setGeometry(100, 100, 300, 200)

layout =  QVBoxLayout()
label = QLabel('Enter you name')
textbox = QLineEdit()
button = QPushButton('Submit')
    
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)

button.clicked.connect(on_submit)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())