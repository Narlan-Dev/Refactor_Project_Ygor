from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

Builder.load_string('''
<DashboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        # Title area
        BoxLayout:
            size_hint_y: None
            height: 100
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex("#2A2E83")
                Rectangle:
                    pos: self.pos
                    size: self.size

            BoxLayout:
                padding: 10, 5
                spacing: 10

                Label:
                    text: 'Rotation'
                    font_size: '36sp'
                    bold: True
                    color: 1, 1, 1, 1
                    size_hint_x: None
                    width: self.texture_size[0]
                    halign: 'left'
                    valign: 'bottom'

                Widget:
                
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    size_hint: None, None
                    size: 320, 40
                    pos_hint: {'center_y': 0.5}

                    RoundedTextInput:
                        id: angle
                        hint_text: 'Turning angle º'

                    RoundedButton:
                        text: 'Submit angle'
                        size_hint: None, None
                        size: 150, 40
                        on_release: root.handle_rotation()

            Label:
                text: 'Boners after rotation'
                font_size: '24sp'
                color: 0.9, 0.9, 1, 1
                size_hint_y: None
                height: 30
                halign: 'left'
                valign: 'top'
                text_size: self.size
                padding: 10, 0

        # Message area
        Label:
            id: message_label
            text: root.message
            size_hint_y: None
            height: 30
            color: (0.9, 0.9, 1, 1) if root.message_type == 'success' else (1, 0.5, 0.5, 1)
            halign: 'center'
            valign: 'center'
            text_size: self.size

        # Main content
        BoxLayout:
            orientation: 'horizontal'
            spacing: 20
            padding: 20, 0

            # Image or message
            BoxLayout:
                id: image_container
                size_hint: None, None
                size: self.parent.width * 0.4, self.parent.width * 0.4

                Label:
                    id: image_placeholder
                    text: 'Image will appear here after submitting an angle'
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

            # Information boxes
            BoxLayout:
                orientation: 'vertical'
                spacing: 15
                size_hint_x: 0.6
                padding: [150, 0, 0, 0]
                
                Label:
                    text: 'title at information'
                    size_hint_y: None
                    height: 30
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

                RoundedLabel:
                    id: test
                    text: 'Information'
                    size_hint_y: None
                    height: 50

                Label:
                    text: 'title at information'
                    size_hint_y: None
                    height: 30
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

                RoundedLabel:
                    id: sigma_x_label
                    text: 'Sigma X:'
                    size_hint_y: None
                    height: 50

                Label:
                    text: 'title at information'
                    size_hint_y: None
                    height: 30
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

                RoundedLabel:
                    id: sigma_y_label
                    text: 'Sigma Y:'
                    size_hint_y: None
                    height: 50

                Label:
                    text: 'title at information'
                    size_hint_y: None
                    height: 30
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

                RoundedLabel:
                    id: txy_label
                    text: 'Txy:'
                    size_hint_y: None
                    height: 50
''')

class DashboardScreen(Screen):
    message = StringProperty('')
    message_type = StringProperty('success')
    image = ObjectProperty(None)

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