from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from styles.style import sidebar_style, button_style, label_style, list_widget_style
import random

class ShowInfos(QWidget):
    def __init__(self, first_name, last_name, email, password, parent=None):
        super().__init__()
        self.parent_window = parent  # Store the reference to the parent window
        self.setWindowTitle("Form Details and Images")
        self.setFixedSize(1280, 720)  # Full HD

        # Main layout: Horizontal split
        main_layout = QHBoxLayout(self)

        # Sidebar container
        sidebar = QWidget(self)
        sidebar_layout = QVBoxLayout(sidebar)

        # Program title with icon at the top of the sidebar
        title_layout = QHBoxLayout()
        icon_label = QLabel()  # Icon placeholder
        icon_label.setPixmap(QPixmap(32, 32))  # Placeholder for icon size
        icon_label.setStyleSheet("background-color: #00bfff; border-radius: 16px;")  # Placeholder color for icon
        title_label = QLabel("Mohr Circle")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
                margin-left: 10px;
            }
        """)
        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)

        sidebar_layout.addLayout(title_layout)
        sidebar_layout.addSpacing(30)  # Spacing below the title

        # Sidebar for form fields
        list_widget = QListWidget(self)
        self.addSidebarItem(list_widget, "Firstname", "icons/qualquer.png")
        self.addSidebarItem(list_widget, "Lastname", "icons/qualquer.png")
        self.addSidebarItem(list_widget, "Email", "icons/qualquer.png")
        self.addSidebarItem(list_widget, "Password", "icons/qualquer.png")
        list_widget.currentRowChanged.connect(self.displayContent)
        list_widget.setStyleSheet(list_widget_style)
        sidebar_layout.addWidget(list_widget)
        sidebar_layout.addStretch()

        # Return button at the bottom of the sidebar
        return_button = QPushButton("Return to Form")
        return_button.setStyleSheet(button_style)
        return_button.clicked.connect(self.returnToFirstScreen)
        sidebar_layout.addWidget(return_button)

        # Styling the sidebar (no border, fixed width)
        sidebar.setStyleSheet(sidebar_style)
        sidebar.setFixedWidth(220)

        # Stacked widget for form data display
        self.content_stack = QStackedWidget(self)

        # Labels for form data
        self.first_name_label = QLabel(f"Firstname: {first_name}")
        self.last_name_label = QLabel(f"Lastname: {last_name}")
        self.email_label = QLabel(f"Email: {email}")
        self.password_label = QLabel(f"Password: {password}")

        # Styling the labels
        self.first_name_label.setStyleSheet(label_style)
        self.last_name_label.setStyleSheet(label_style)
        self.email_label.setStyleSheet(label_style)
        self.password_label.setStyleSheet(label_style)

        # Add the labels to the stack
        self.content_stack.addWidget(self.first_name_label)
        self.content_stack.addWidget(self.last_name_label)
        self.content_stack.addWidget(self.email_label)
        self.content_stack.addWidget(self.password_label)

        # Random images layout
        image_layout = QVBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(640, 480)  # Image size
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #333;
                border: 1px solid rgba(105, 105, 105, 0.397);
                border-radius: 10px;
            }
        """)
        self.loadRandomImage()  # Load the first image

        # Next/Previous buttons to swipe images
        next_button = QPushButton("Next Image")
        prev_button = QPushButton("Previous Image")
        next_button.clicked.connect(self.loadNextImage)
        prev_button.clicked.connect(self.loadPreviousImage)

        next_button.setStyleSheet(button_style)
        prev_button.setStyleSheet(button_style)

        # Add image and buttons to layout
        image_layout.addWidget(self.image_label)
        image_layout.addWidget(prev_button)
        image_layout.addWidget(next_button)

        # Add sidebar, form content, and image layout to the main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.content_stack)
        main_layout.addLayout(image_layout)

        # List of random images (placeholders)
        self.image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]
        self.current_image_index = 0

        # Set window background similar to the first screen
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                color: #fff;
                font-family: Arial, sans-serif;
            }
        """)
        
    def addSidebarItem(self, list_widget, label_text, icon_path):
        """Add a sidebar item with an icon to the QListWidget"""
        item = QListWidgetItem(QIcon(icon_path), label_text)
        list_widget.addItem(item)
    
    def displayContent(self, index):
        # Switch the displayed form field content
        self.content_stack.setCurrentIndex(index)

    def loadRandomImage(self):
        # Load a random image (using random colors for this example)
        pixmap = QPixmap(640, 480)
        pixmap.fill(Qt.green if random.randint(0, 1) else Qt.red)
        self.image_label.setPixmap(pixmap)

    def loadNextImage(self):
        # Load the next image in the list
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.loadRandomImage()

    def loadPreviousImage(self):
        # Load the previous image in the list
        self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
        self.loadRandomImage()

    def returnToFirstScreen(self):
        self.close()  # Close the current window
        self.parent_window.show()  # Show the parent window (RegistrationForm)
