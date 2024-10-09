from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.app import App
from views.main_view.main_window import MainWindow

Builder.load_string(''' 
<RegistrationForm>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        CardWidget:
            orientation: 'vertical'
            size_hint: None, None
            size: 500, 500
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            BoxLayout:
                size_hint_y: None
                height: 90
                spacing: 10
                
                Image:
                    source: 'icons/logo.png'
                    size_hint: None, None
                    size: 90, 90
                    
                TitleLabel:
                    text: 'Círculo de Mohr'
                    font_size: '40sp'

            BoxLayout:
                orientation: 'vertical'
                spacing: 30
                padding: [0, 20]

                # Pairing labels and text inputs
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    size_hint_y: None
                    height: 40

                    StylizedLabel:
                        text: 'Tensão σx'
                        size_hint_x: None
                        width: 150  # Fixed width for alignment

                    StylizedTextInput:
                        id: sigma_x
                        hint_text: 'MPa'
                        size_hint_x: 1  # Fill the remaining space

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    size_hint_y: None
                    height: 40

                    StylizedLabel:
                        text: 'Tensão σy'
                        size_hint_x: None
                        width: 150  # Fixed width for alignment

                    StylizedTextInput:
                        id: sigma_y
                        hint_text: 'MPa'
                        size_hint_x: 1  # Fill the remaining space

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    size_hint_y: None
                    height: 40

                    StylizedLabel:
                        text: 'Tensão τxy'
                        size_hint_x: None
                        width: 150  # Fixed width for alignment

                    StylizedTextInput:
                        id: txy
                        hint_text: 'MPa'
                        size_hint_x: 1  # Fill the remaining space

            StylizedButton:
                text: 'SUBMETER'
                pos_hint: {'center_x': 0.5}
                on_release: root.open_next_screen()
''')


class RegistrationForm(FloatLayout):
    def validate_inputs(self):
        try:
            float(self.ids.sigma_x.text)
            float(self.ids.sigma_y.text)
            float(self.ids.txy.text)
            return True
        except ValueError:
            popup = Popup(
                title='Input Error',
                content=Label(text='Please enter valid numerical values for all fields.'),
                size_hint=(None, None),
                size=(400, 200)
            )
            popup.open()
            return False

    def open_next_screen(self):
        if self.validate_inputs():
            app = App.get_running_app()
            sm = app.root
            
            main_window = MainWindow(
                sigma_x=self.ids.sigma_x.text,
                sigma_y=self.ids.sigma_y.text,
                txy=self.ids.txy.text,
                previous_screen=self  # Pass the current screen as previous
            )

            sm.get_screen('main').clear_widgets()
            sm.get_screen('main').add_widget(main_window)
            sm.current = 'main'