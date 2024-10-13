from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.metrics import dp
import os

Builder.load_string('''
<CircleView>:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    
    Image:
        id: image_display
        source: ''
        allow_stretch: True
        keep_ratio: True
        size_hint: 1, 0.9
        
    BoxLayout:
        size_hint_y: 0.1
        padding: dp(10)
        spacing: dp(10)
        
        NavigationButton:
            text: '<'
            on_release: root.previous_image()
            size_hint_x: None
            width: self.height

        Label:
            id: step_label
            text: 'STEP: 0'
            size_hint_x: 1
            canvas.before:
                Color:
                    rgba: 0.231, 0.282, 0.761, 1  # #3B48C2
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(5),]

        NavigationButton:
            text: '>'
            on_release: root.next_image()
            size_hint_x: None
            width: self.height

<NavigationButton@Button>:
    background_color: 0.231, 0.282, 0.761, 1  # #3B48C2
    color: 1, 1, 1, 1
    size_hint: None, None
    size: dp(40), dp(40)
    font_size: dp(20)
''')

class CircleView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_image_index = 0
        self.image_paths = []
        self.load_image_folder()
        
    def load_image_folder(self):
        folder_path = 'public'
        if os.path.exists(folder_path):
            self.image_paths = [
                os.path.join(folder_path, f) 
                for f in os.listdir(folder_path) 
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
            ]
            if self.image_paths:
                self.load_image()
                
    def load_image(self):
        if self.image_paths:
            self.ids.image_display.source = self.image_paths[self.current_image_index]
            self.ids.step_label.text = f'STEP: {self.current_image_index + 1}'
            
    def next_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.load_image()
            
    def previous_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.load_image()