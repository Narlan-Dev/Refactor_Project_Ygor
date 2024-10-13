from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.core.window import Window

Builder.load_string('''
<RotationAngleScreen>:
    is_mobile: app.is_mobile() if hasattr(app, 'is_mobile') else False
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        # Title area
        BoxLayout:
            size_hint_y: None
            height: dp(100) if not root.is_mobile else dp(80)
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex("#2A2E83")
                Rectangle:
                    pos: self.pos
                    size: self.size

            BoxLayout:
                orientation: 'horizontal'
                padding: dp(10), dp(5)
                spacing: dp(10)

                Label:
                    text: 'Rotation'
                    font_size: sp(28) if root.is_mobile else sp(36)
                    bold: True
                    color: 1, 1, 1, 1
                    size_hint_x: None
                    width: self.texture_size[0]
                    halign: 'left'
                    valign: 'center'

                Widget:
                    size_hint_x: 0.1 if root.is_mobile else 0.3

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(10)
                    size_hint: (0.9, None) if root.is_mobile else (0.6, None)
                    height: dp(40)
                    pos_hint: {'center_y': 0.5}

                    RoundedTextInput:
                        id: angle
                        hint_text: 'Turning angle º'
                        size_hint_x: 0.6

                    RoundedButton:
                        size_hint_x: 0.2
                        on_release: root.handle_rotation()
                        BoxLayout:
                            pos: self.parent.pos
                            size: self.parent.size
                            Image:
                                source: 'icons/qualquer.png'
                                center_y: root.center_y
                                size: dp(20), dp(20)
                                opacity: 1 if root.is_mobile else 0
                            Label:
                                text: 'Submit'
                                font_size: sp(14)
                                color: 1, 1, 1, 1
                                size_hint: (None, 1) if not root.is_mobile else (0, 0)
                                opacity: 0 if root.is_mobile else 1

            Label:
                text: 'Boners after rotation'
                font_size: sp(18) if root.is_mobile else sp(24)
                color: 0.9, 0.9, 1, 1
                size_hint_y: None
                height: dp(30)
                halign: 'left'
                valign: 'top'
                text_size: self.size
                padding: dp(10), 0

        # Message area
        Label:
            id: message_label
            text: root.message
            size_hint_y: None
            height: dp(30)
            color: (0.9, 0.9, 1, 1) if root.message_type == 'success' else (1, 0.5, 0.5, 1)
            halign: 'center'
            valign: 'center'
            text_size: self.size

        # Main content
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10), 0

            # Image or message
            BoxLayout:
                id: image_container
                size_hint: (1, 0.5)
                height: min(root.height * 0.3, dp(300)) if root.is_mobile else min(root.width * 0.4, dp(400))

                Label:
                    id: image_placeholder
                    text: 'Image will appear here after submitting an angle'
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

            # Information boxes
            ScrollView:
                size_hint: (1, 0.5)
                do_scroll_x: False
                do_scroll_y: True

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    padding: 0, dp(10)
                    
                    Label:
                        text: 'Information'
                        size_hint_y: None
                        height: dp(30)
                        color: 0.9, 0.9, 1, 1
                        halign: 'center'
                        valign: 'center'
                        text_size: self.size

                    RoundedLabel:
                        id: test
                        text: 'Information'
                        size_hint_y: None
                        height: dp(50)

                    Label:
                        text: 'Sigma X'
                        size_hint_y: None
                        height: dp(30)
                        color: 0.9, 0.9, 1, 1
                        halign: 'center'
                        valign: 'center'
                        text_size: self.size

                    RoundedLabel:
                        id: sigma_x_label
                        text: 'Sigma X:'
                        size_hint_y: None
                        height: dp(50)

                    Label:
                        text: 'Sigma Y'
                        size_hint_y: None
                        height: dp(30)
                        color: 0.9, 0.9, 1, 1
                        halign: 'center'
                        valign: 'center'
                        text_size: self.size

                    RoundedLabel:
                        id: sigma_y_label
                        text: 'Sigma Y:'
                        size_hint_y: None
                        height: dp(50)

                    Label:
                        text: 'Txy'
                        size_hint_y: None
                        height: dp(30)
                        color: 0.9, 0.9, 1, 1
                        halign: 'center'
                        valign: 'center'
                        text_size: self.size

                    RoundedLabel:
                        id: txy_label
                        text: 'Txy:'
                        size_hint_y: None
                        height: dp(50)
''')

class RotationAngleScreen(Screen):
    message = StringProperty('')
    message_type = StringProperty('success')
    image = ObjectProperty(None)
    is_mobile = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(size=self.check_window_size)
        self.check_window_size()
    
    
    def update_information(self, sigma_x, sigma_y, txy):
        if sigma_x:
            self.ids.test.text = f"Test: {int(sigma_x) - 1}"
            
        self.ids.sigma_x_label.text = f"Sigma X: {sigma_x}"
        self.ids.sigma_y_label.text = f"Sigma Y: {sigma_y}"
        self.ids.txy_label.text = f"Txy: {txy}"
        
    def handle_rotation(self):
        if self.ids.angle.text:
            try:
                angle = int(self.ids.angle.text)
                self.ids.test.text = f"Test: {int(self.ids.test.text.split(': ')[1]) + angle}"
                self.ids.sigma_x_label.text = f"Sigma X: {int(self.ids.sigma_x_label.text.split(': ')[1]) + angle}"
                self.ids.sigma_y_label.text = f"Sigma Y: {int(self.ids.sigma_y_label.text.split(': ')[1]) + angle}"
                self.ids.txy_label.text = f"Txy: {int(self.ids.txy_label.text.split(': ')[1]) + angle}"
                self.message = "Rotation applied successfully!"
                self.message_type = 'success'
                self.load_image()
            except ValueError:
                self.message = "Error: Please enter a valid integer for the angle."
                self.message_type = 'error'
        else:
            self.message = "Error: Please enter an angle before submitting."
            self.message_type = 'error'
        
        # Schedule the message to be cleared after 5 seconds
        Clock.schedule_once(self.clear_message, 5)

    def clear_message(self, dt):
        self.message = ''
        self.message_type = 'success'  # Reset to default state

    def load_image(self):
        from kivy.uix.image import Image
        if self.image:
            self.ids.image_container.remove_widget(self.image)
        self.image = Image(source='public/teste1.png', allow_stretch=True, keep_ratio=True)
        self.ids.image_container.clear_widgets()
        self.ids.image_container.add_widget(self.image)
        
    def check_window_size(self, *args):
        self.is_mobile = Window.width < dp(600)