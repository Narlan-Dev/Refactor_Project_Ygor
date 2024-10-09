from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
import os

Builder.load_string('''
<CircleView>:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    
    Image:
        id: image_display
        source: ''
        allow_stretch: True
        keep_ratio: True
        
    BoxLayout:
        size_hint_y: None
        height: 50
        spacing: 20
        FloatLayout:
            center_x: self.parent.center_x
            center_y: self.parent.center_y
            
            #Steps layout
            BoxLayout:
                size_hint: None, None
                size: self.minimum_size
                center_x: self.parent.center_x
                orientation: 'horizontal'
                spacing: 100
                padding: 10

                NavigationButton:
                    text: '<'
                    on_release: root.previous_image()

                Label:
                    id: step_label
                    text: 'STEP: 0'
                    size_hint_x: None
                    width: 200
                    canvas.before:
                        Color:
                            rgba: 0.231, 0.282, 0.761, 1  # #3B48C2
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [5,]

                NavigationButton:
                    text: '>'
                    on_release: root.next_image()
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