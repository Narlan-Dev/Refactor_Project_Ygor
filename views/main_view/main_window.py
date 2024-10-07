import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                             QFileDialog, QStackedWidget, QLineEdit, QTextEdit, QGridLayout, QSlider, QComboBox,
                             QProgressBar, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer, QSize
from styles.style import (main_window_style)
from views.main_view.circle_view import CircleView

class MainWindow(QMainWindow):
    def __init__(self, sigma_x=None, sigma_y=None, txy=None, parent=None):
        super().__init__()
        self.parent = parent
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        self.txy = txy
        
        self.setWindowTitle("Multi-functional App")
        self.setStyleSheet(main_window_style)
        
        self.current_selected_button = None

        # Set the resolution to Full HD
        self.resize(1280, 720)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        sidebar_title = QLabel("Menu")
        sidebar_title.setObjectName("sidebar-title")
        sidebar_title.setFont(QFont("Arial", 16, QFont.Bold))
        sidebar_title.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(sidebar_title)

        # Folder for icons
        icon_folder = "icons/"

        # Store buttons in a list for easy access
        self.nav_buttons = []
        nav_buttons = [
            ("Dashboard", "qualquer.png", self.show_dashboard),
            ("Circle Mohr", "qualquer.png", self.show_circle),
            ("User", "qualquer.png", self.show_user_profile),
            ("Settings", "qualquer.png", self.show_settings)
        ]

        for text, icon_name, func in nav_buttons:
            icon_path = os.path.join(icon_folder, icon_name)
            btn = QPushButton(f"  {text}")
            if os.path.exists(icon_path):
                btn.setIcon(QIcon(icon_path)) 
                btn.setIconSize(QSize(24, 24))
            btn.clicked.connect(lambda checked, b=btn, f=func: self.on_nav_button_clicked(b, f))
            sidebar_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        sidebar_layout.addStretch()

        return_button = QPushButton("Return")
        return_button.setObjectName("return-button")
        return_button.clicked.connect(self.return_to_registration)
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
        #Make the same with others views
        self.circle_view = CircleView()
        self.content.addWidget(self.circle_view)
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

    def show_circle(self):
        self.content.setCurrentIndex(1)

    def show_user_profile(self):
        self.content.setCurrentIndex(2)

    def show_settings(self):
        self.content.setCurrentIndex(3)

    def show_message(self, message):
        msg = QLabel(message)
        msg.setStyleSheet("color: green; font-weight: bold;")
        self.statusBar().addWidget(msg)
        QTimer.singleShot(3000, lambda: self.statusBar().removeWidget(msg))
        
    def return_to_registration(self):
        """Handle return button click to go back to RegistrationForm"""
        if self.parent:
            self.parent.show()
            self.close()