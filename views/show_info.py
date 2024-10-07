from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from styles.style import sidebar_style, button_style, label_style, list_widget_style, arrow_button_style
import os

class ShowInfos(QWidget):
    def __init__(self, sigma_x_input, sigma_y_input, txy_input, parent=None):
        super().__init__()
        self.parent_window = parent
        self.setWindowTitle("Form Details and Images")
        self.setFixedSize(1280, 720)

        # Main layout: Horizontal split
        main_layout = QHBoxLayout(self)

        # Sidebar container
        sidebar = QWidget(self)
        sidebar_layout = QVBoxLayout(sidebar)

        # Program title with icon at the top of the sidebar
        title_layout = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(32, 32))
        icon_label.setStyleSheet("background-color: #00bfff; border-radius: 16px;") 
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
        sidebar_layout.addSpacing(30)

        # Sidebar for form fields
        list_widget = QListWidget(self)
        self.addSidebarItem(list_widget, "Firstname", "icons/qualquer.png")
        self.addSidebarItem(list_widget, "Lastname", "icons/qualquer.png")
        self.addSidebarItem(list_widget, "Email", "icons/qualquer.png")
        list_widget.currentRowChanged.connect(self.displayContent)
        list_widget.setStyleSheet(list_widget_style)
        list_widget.setFocusPolicy(Qt.NoFocus)
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
        self.content_stack.setStyleSheet("""
            QStackedWidget {
                background-color: transparent;
                border: none;
            }
        """)
        
        # Labels for form data
        self.first_name_label = QLabel(f"Firstname: {sigma_x_input}")
        self.last_name_label = QLabel(f"Lastname: {sigma_y_input}")
        self.email_label = QLabel(f"Email: {txy_input}")

        # Styling the labels
        self.first_name_label.setStyleSheet(label_style)
        self.last_name_label.setStyleSheet(label_style)
        self.email_label.setStyleSheet(label_style)

        # Add the labels to the stack
        self.content_stack.addWidget(self.first_name_label)
        self.content_stack.addWidget(self.last_name_label)
        self.content_stack.addWidget(self.email_label)

        # Images layout
        image_layout = QVBoxLayout()
        image_layout.setContentsMargins(0, 0, 0, 0)
        button_grid = QGridLayout()
        
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(640, 480)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: transparent;
                border: none
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);  /* Adiciona uma sombra para profundidade */
            }
        """)
        self.image_paths = self.loadImagePaths("public/")  # Replace with the directory where images are stored
        self.current_image_index = 0
        self.loadImage()

        # Next/Previous buttons to swipe images
        next_button = QPushButton("→")
        prev_button = QPushButton("←")
        next_button.clicked.connect(self.loadNextImage)
        prev_button.clicked.connect(self.loadPreviousImage)

        next_button.setStyleSheet(arrow_button_style)
        prev_button.setStyleSheet(arrow_button_style)
        
        button_grid.addWidget(prev_button, 0, 0, Qt.AlignLeft | Qt.AlignBottom) 
        button_grid.addWidget(next_button, 0, 1, Qt.AlignRight | Qt.AlignBottom)
        button_grid.setColumnStretch(0, 1)
        button_grid.setColumnStretch(1, 1)
        
        # Add image and buttons to layout
        image_layout.addWidget(self.image_label)
        image_layout.addLayout(button_grid)

        # Add sidebar, form content, and image layout to the main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.content_stack)
        main_layout.addLayout(image_layout)
        
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

    def loadImagePaths(self, directory):
        """Load all image paths from the given directory."""
        valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
        return [os.path.join(directory, file) for file in os.listdir(directory)
                if os.path.splitext(file)[1].lower() in valid_extensions]

    def loadImage(self):
        """Load the current image based on the current_image_index."""
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def loadNextImage(self):
        if not self.image_paths:
            print("No images found.")
            return 
        
        # Update the index safely
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.loadImage()

    def loadPreviousImage(self):
        if not self.image_paths:
            print("No images found.")
            return

        # Update the index safely
        self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
        self.loadImage()

    def returnToFirstScreen(self):
        self.close()  # Close the current window
        self.parent_window.show()
