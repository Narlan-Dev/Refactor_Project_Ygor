import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Example")
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #2A2E83;
            }
            QLabel {
                color: white;
            }
            QLabel#info_label {
                background-color: #6495ED;
                border-radius: 15px;
                padding: 10px;
                font-size: 18px;
                qproperty-alignment: AlignCenter;
            }
            QPushButton#back_button {
                background-color: transparent;
                color: #E6E6FA;
                font-size: 16px;
            }
            QWidget#header_widget {
                background-color: #4169E1;
                border-radius: 15px;
            }
            QLabel#title_label, QLabel#subtitle_label {
                background-color: transparent;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)

        # Header
        header_widget = QWidget()
        header_widget.setObjectName("header_widget")
        header_layout = QHBoxLayout(header_widget)
        header_layout.setSpacing(0)
        header_layout.setContentsMargins(50, 50, 50, 50)
        
        title_layout = QVBoxLayout()
        title_layout.setSpacing(10)
        
        title = QLabel("Title")
        title.setObjectName("title_label")
        title.setFont(QFont("Arial", 36, QFont.Bold))
        title.setStyleSheet("color: #E6E6FA;")
        title_layout.addWidget(title)
        
        subtitle = QLabel("Sub Title")
        subtitle.setObjectName("subtitle_label")
        subtitle.setFont(QFont("Arial", 24))
        subtitle.setStyleSheet("color: #E6E6FA;")
        title_layout.addWidget(subtitle)
        
        header_layout.addLayout(title_layout)
        header_layout.addStretch(1)
        back_button = QPushButton("Button to back")
        back_button.setObjectName("back_button")
        header_layout.addWidget(back_button, alignment=Qt.AlignTop)
        
        main_layout.addWidget(header_widget)
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Content
        content_layout = QHBoxLayout()
        content_layout.setSpacing(0)  # Remove default spacing
        content_layout.setContentsMargins(50,50,50,50)
        
        # Image placeholder (enlarged by 30%)
        image_size = int(200 * 1.3)  # 30% larger
        image_label = QLabel()
        image_label.setFixedSize(image_size, image_size)
        image_label.setStyleSheet("background-color: white; border-radius: 26px;")  # Increased border radius
        content_layout.addWidget(image_label)

        # Add spacer to separate image from information labels
        content_layout.addItem(QSpacerItem(int(1280 * 0.5), 20, QSizePolicy.Fixed, QSizePolicy.Minimum))

        # Information labels
        info_layout = QVBoxLayout()
        info_layout.setSpacing(20)
        for i in range(3):
            info_item_layout = QVBoxLayout()
            info_item_layout.setSpacing(5)
            
            title_label = QLabel("title at information")
            title_label.setStyleSheet("color: #E6E6FA; font-size: 16px;")
            title_label.setAlignment(Qt.AlignCenter)
            info_item_layout.addWidget(title_label)
            
            info_label = QLabel("Information")
            info_label.setObjectName("info_label")
            info_label.setFixedHeight(50)
            info_item_layout.addWidget(info_label)
            
            info_layout.addLayout(info_item_layout)

        content_layout.addLayout(info_layout)

        main_layout.addLayout(content_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1280, 720)  # HD resolution
    window.show()
    sys.exit(app.exec_())