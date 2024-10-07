from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton,QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class CircleView(QWidget):
    def __init__(self):
      super().__init__()
      self.current_image_index = 0
      self.image_paths = []
      self.init_ui()
      
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.image_label = QLabel("No images loaded. Click 'Load Image Folder' to start.")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        self.steps = QLabel(f'STEP: {self.current_image_index}')
        self.steps.setObjectName('steps')
           
        nav_layout = QHBoxLayout()
        nav_prev = QPushButton("<")
        nav_next = QPushButton(">")
        nav_prev.setObjectName("nav-button")
        nav_next.setObjectName("nav-button")
        nav_prev.clicked.connect(self.previous_image)
        nav_next.clicked.connect(self.next_image)
        nav_layout.addWidget(nav_prev)
        nav_layout.addStretch()
        nav_layout.addWidget(self.steps)
        nav_layout.addStretch()
        nav_layout.addWidget(nav_next)

        layout.addLayout(nav_layout)
        self.load_image_folder()
        #load_folder_button = QPushButton("Load Image Folder")
        #load_folder_button.setObjectName('loader_folder')
        #load_folder_button.clicked.connect(self.load_image_folder)
        #layout.addWidget(load_folder_button)

    def load_image_folder(self):
        folder_path = 'public' #QFileDialog.getExistingDirectory(self, "Select Image Folder")
        if folder_path:
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
            self.current_image_index = 0
            self.load_image()
        
    def load_image(self):
        if self.image_paths:
            pixmap = QPixmap(self.image_paths[self.current_image_index])
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.steps.setText(f'STEP: {self.current_image_index}')
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