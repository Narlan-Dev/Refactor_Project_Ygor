import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                             QFileDialog, QStackedWidget, QLineEdit, QTextEdit, QGridLayout, QSlider, QComboBox,
                             QProgressBar, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-functional App")
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #2A2E83;
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton {
                background-color: transparent;
                color: white;
                text-align: left;
                padding: 15px 20px;
                border: none;
                font-size: 16px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                transition: background-color 0.3s ease-in-out, transform 0.2s;
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.1);
                transform: scale(0.98);
            }
            QPushButton[selected="true"] {
                background-color: rgba(255, 255, 255, 0.4);
                border-radius: 10px;
                font-weight: bold;
            }
            #sidebar {
                background-color: #343AEB;
                border-top-left-radius: 20px;
                border-bottom-left-radius: 20px;
                padding-top: 20px;
            }
            #content {
                background-color: white;
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;
            }
            QLabel#sidebar-title {
                background-color: none;
                font-size: 24px;
                font-weight: 600;
                padding: 10px;
                text-align: center;
            }
            QPushButton#nav-button {
                font-size: 24px;
                padding: 10px;
                background-color: #2A2E83;
                border-radius: 5px;
                color: white;
            }
            #return-button {
                background-color: #4C5CD2;
                border-radius: 8px;
                padding: 15px;
                font-size: 16px;
                color: white;
                margin: 20px;
            }
            #return-button:hover {
                background-color: #3B48C2;
                transition: background-color 0.3s ease-in-out;
            }
            QPushButton#return-button {
                font-weight: 500;
            }
        """)

        self.image_paths = []
        self.current_image_index = 0
        self.current_selected_button = None  # To track the selected button

        # Set the resolution to Full HD
        self.resize(1280, 720)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        main_layout.setSpacing(0)  # Remove spacing

        # Sidebar
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Ensure sidebar fills vertical space

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        sidebar_layout.setSpacing(0)  # Remove spacing

        sidebar_title = QLabel("Menu")
        sidebar_title.setObjectName("sidebar-title")
        sidebar_title.setFont(QFont("Arial", 16, QFont.Bold))
        sidebar_title.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(sidebar_title)

        # Folder for icons
        icon_folder = "icons/"  # Specify the path to your icons folder here

        # Store buttons in a list for easy access
        self.nav_buttons = []
        nav_buttons = [
            ("Dashboard", "qualquer.png", self.show_dashboard),
            ("Image", "qualquer.png", self.show_image_gallery),
            ("User", "qualquer.png", self.show_user_profile),
            ("Settings", "qualquer.png", self.show_settings)
        ]

        for text, icon_name, func in nav_buttons:
            icon_path = os.path.join(icon_folder, icon_name)
            btn = QPushButton(f"  {text}")
            if os.path.exists(icon_path):  # Check if the icon file exists
                btn.setIcon(QIcon(icon_path))  # Set the icon for the button
                btn.setIconSize(QSize(24, 24))  # Set the icon size
            btn.clicked.connect(lambda checked, b=btn, f=func: self.on_nav_button_clicked(b, f))
            sidebar_layout.addWidget(btn)
            self.nav_buttons.append(btn)  # Add each button to the list

        sidebar_layout.addStretch()

        return_button = QPushButton("Return")
        return_button.setObjectName("return-button")
        sidebar_layout.addWidget(return_button)

        # Content area
        self.content = QStackedWidget()
        self.content.setObjectName("content")

        # Add sidebar and content to main layout
        main_layout.addWidget(sidebar, 1)
        main_layout.addWidget(self.content, 3)

        # Set the main layout to a central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Initialize views
        self.init_dashboard()
        self.init_image_gallery()
        self.init_user_profile()
        self.init_settings()

        # Show dashboard by default and highlight it
        self.show_dashboard()
        self.highlight_button(self.nav_buttons[0])

    def init_dashboard(self):
        dashboard = QWidget()
        layout = QVBoxLayout(dashboard)

        layout.addWidget(QLabel("Simple Dashboard"))

        # Add some sample widgets to the dashboard
        progress_bar = QProgressBar()
        progress_bar.setValue(75)
        layout.addWidget(QLabel("Sample Progress:"))
        layout.addWidget(progress_bar)

        layout.addWidget(QLabel("Quick Actions:"))
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Action 1"))
        actions_layout.addWidget(QPushButton("Action 2"))
        actions_layout.addWidget(QPushButton("Action 3"))
        layout.addLayout(actions_layout)

        layout.addStretch()

        self.content.addWidget(dashboard)

    def init_image_gallery(self):
        gallery = QWidget()
        layout = QVBoxLayout(gallery)

        self.image_label = QLabel("No images loaded. Click 'Load Image Folder' to start.")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        nav_layout = QHBoxLayout()
        nav_prev = QPushButton("<")
        nav_next = QPushButton(">")
        nav_prev.setObjectName("nav-button")
        nav_next.setObjectName("nav-button")
        nav_prev.clicked.connect(self.previous_image)
        nav_next.clicked.connect(self.next_image)
        nav_layout.addWidget(nav_prev)
        nav_layout.addStretch()
        nav_layout.addWidget(nav_next)

        layout.addLayout(nav_layout)

        load_folder_button = QPushButton("Load Image Folder")
        load_folder_button.clicked.connect(self.load_image_folder)
        layout.addWidget(load_folder_button)

        self.content.addWidget(gallery)

    def init_user_profile(self):
        profile = QWidget()
        layout = QGridLayout(profile)

        layout.addWidget(QLabel("Name:"), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        layout.addWidget(QLabel("Email:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        layout.addWidget(QLabel("Bio:"), 2, 0)
        layout.addWidget(QTextEdit(), 2, 1)

        save_button = QPushButton("Save Profile")
        save_button.clicked.connect(lambda: self.show_message("Profile saved!"))
        layout.addWidget(save_button, 3, 1)

        self.content.addWidget(profile)

    def init_settings(self):
        settings = QWidget()
        layout = QVBoxLayout(settings)

        layout.addWidget(QLabel("Theme:"))
        theme_combo = QComboBox()
        theme_combo.addItems(["Light", "Dark", "System"])
        layout.addWidget(theme_combo)

        layout.addWidget(QLabel("Notification Sound:"))
        sound_slider = QSlider(Qt.Horizontal)
        layout.addWidget(sound_slider)

        save_button = QPushButton("Save Settings")
        save_button.clicked.connect(lambda: self.show_message("Settings saved!"))
        layout.addWidget(save_button)

        self.content.addWidget(settings)

    def on_nav_button_clicked(self, button, func):
        # Highlight the selected button
        self.highlight_button(button)
        # Call the function associated with the button
        func()

    def highlight_button(self, button):
        # Reset the style of the previously selected button
        if self.current_selected_button:
            self.current_selected_button.setProperty('selected', False)
            self.current_selected_button.setStyle(self.current_selected_button.style())
        
        # Set the new button as selected
        self.current_selected_button = button
        self.current_selected_button.setProperty('selected', True)
        self.current_selected_button.setStyle(self.current_selected_button.style())

    def show_dashboard(self):
        self.content.setCurrentIndex(0)

    def show_image_gallery(self):
        self.content.setCurrentIndex(1)

    def show_user_profile(self):
        self.content.setCurrentIndex(2)

    def show_settings(self):
        self.content.setCurrentIndex(3)

    def load_image_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Image Folder")
        if folder_path:
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
            self.current_image_index = 0
            self.load_image()

    def load_image(self):
        if self.image_paths:
            pixmap = QPixmap(self.image_paths[self.current_image_index])
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.image_label.setText("No images loaded.")

    def next_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.load_image()

    def previous_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.load_image()

    def show_message(self, message):
        msg = QLabel(message)
        msg.setStyleSheet("color: green; font-weight: bold;")
        self.statusBar().addWidget(msg)
        QTimer.singleShot(3000, lambda: self.statusBar().removeWidget(msg))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
