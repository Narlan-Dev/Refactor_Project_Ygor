from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

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
                    text: 'Title'
                    font_size: '36sp'
                    bold: True
                    color: 1, 1, 1, 1
                    size_hint_x: None
                    width: self.texture_size[0]
                    halign: 'left'
                    valign: 'bottom'

                Widget:

                RoundedButton:
                    text: 'Button to back'
                    size_hint: None, None
                    size: 150, 40
                    pos_hint: {'center_y': 0.5}

            Label:
                text: 'Sub Title'
                font_size: '24sp'
                color: 0.9, 0.9, 1, 1
                size_hint_y: None
                height: 30
                halign: 'left'
                valign: 'top'
                text_size: self.size
                padding: 10, 0

        # Main content
        BoxLayout:
            orientation: 'horizontal'
            spacing: 20
            padding: 20, 0

            # Image
            Image:
                source: 'public/teste1.png'  # Replace with your image path
                size_hint: None, None
                size: self.parent.width * 0.4, self.parent.width * 0.4
                allow_stretch: True
                keep_ratio: True

            # Information boxes
            BoxLayout:
                orientation: 'vertical'
                spacing: 15
                size_hint_x: 0.6

                Label:
                    text: 'title at information'
                    size_hint_y: None
                    height: 30
                    color: 0.9, 0.9, 1, 1
                    halign: 'center'
                    valign: 'center'
                    text_size: self.size

                RoundedButton:
                    id: sigma_x_button
                    text: 'Sigma X: '
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

                RoundedButton:
                    id: sigma_y_button
                    text: 'Sigma Y: '
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

                RoundedButton:
                    id: txy_button
                    text: 'Txy: '
                    text: 'Information'
                    size_hint_y: None
                    height: 50
''')

class DashboardScreen(Screen):
    def update_information(self, sigma_x, sigma_y, txy):
        self.ids.sigma_x_button.text = f"Sigma X: {sigma_x}"
        self.ids.sigma_y_button.text = f"Sigma Y: {sigma_y}"
        self.ids.txy_button.text = f"Txy: {txy}"