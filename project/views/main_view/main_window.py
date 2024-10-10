from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty
from views.main_view.circle_view import CircleView
from views.main_view.info_view import InfoScreen
from views.main_view.dash_board_view import DashboardScreen
from styles import colors

Builder.load_string('''
#:import utils kivy.utils

<RoundedButton@Button>:
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1") if self.state == "normal" else utils.get_color_from_hex("#3A5FCC")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]
            
<RoundedLabel@Label>:
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]
            
<RoundedTextInput@TextInput>:
    background_color: 0, 0, 0, 0
    cursor_color: 1, 1, 1, 1
    foreground_color: 1, 1, 1, 1
    hint_text_color: 1, 1, 1, 0.7 
    selection_color: 0.22, 0.33, 0.7, 0.5 
    padding: [10, 10]
    size_hint: None, None
    size: 150, 40
    multiline: False
    halign: 'center'
    valign: 'middle'

<MainWindow>:
    dashboard_button: dashboard_button
    circle_button: circle_button
    info_button: info_button
    settings_button: settings_button

    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#2A2E83")
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: 'horizontal'
        spacing: 0
        padding: 0
        
        # Sidebar
        BoxLayout:
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex("#4169E1")
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [0, 20, 20, 0]
            
            orientation: 'vertical'
            size_hint_x: 0.25
            padding: 20
            spacing: 10

            Label:
                text: 'Menu'
                font_size: '24sp'
                size_hint_y: None
                height: 50
                bold: True
                padding: [0, 0, 150, 0]

            # MenuButton with icons
            BoxLayout:
                orientation:'vertical'
                size_hint_y: None
                height: 250
                spacing: 10
                
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 50
                    spacing: 10
                    
                    Image:
                        source: 'icons/qualquer.png'
                        size_hint_x: None
                        width: 30
                        
                    MenuButton:
                        id: dashboard_button
                        text: 'Rotate'
                        on_release: 
                            root.show_screen('dashboard')
                            root.select_button(self)

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 50
                    spacing: 10

                    Image:
                        source: 'icons/qualquer.png'
                        size_hint_x: None
                        width: 30

                    MenuButton:
                        id: circle_button
                        text: 'Circle Mohr'
                        on_release: 
                            root.show_screen('circle')
                            root.select_button(self)

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 50
                    spacing: 10

                    Image:
                        source: 'icons/qualquer.png'
                        size_hint_x: None
                        width: 30

                    MenuButton:
                        id: info_button
                        text: 'Info'
                        on_release: 
                            root.show_screen('info')
                            root.select_button(self)

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 50
                    spacing: 10

                    Image:
                        source: 'icons/qualquer.png'
                        size_hint_x: None
                        width: 30

                    MenuButton:
                        id: settings_button
                        text: 'Settings'
                        on_release: 
                            root.show_screen('settings')
                            root.select_button(self)
                
            Widget:
                # Spacer

            Button:
                text: 'Return'
                size_hint_y: None
                height: 50
                background_color: 0, 0, 0, 0
                on_release: root.return_to_registration()
                canvas.before:
                    Color:
                        rgba: 0.298, 0.361, 0.824, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, ]
                
        # Content Area
        ScreenManager:
            id: screen_manager
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex("#2A2E83")
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [0, 20, 20, 0]
''')

class MainWindow(BoxLayout):
    dashboard_button = ObjectProperty(None)
    circle_button = ObjectProperty(None)
    info_button = ObjectProperty(None)
    settings_button = ObjectProperty(None)

    def __init__(self, sigma_x=None, sigma_y=None, txy=None, previous_screen=None, **kwargs):
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        self.txy = txy
        self.previous_screen = previous_screen
        self.selected_button = None
        super().__init__(**kwargs)
        
        # Initialize screens
        self.init_screens()
        
    def init_screens(self):
        sm = self.ids.screen_manager
        
        # Dashboard screen
        dashboard = DashboardScreen(name='dashboard')
        dashboard.update_information(self.sigma_x, self.sigma_y, self.txy)
        sm.add_widget(dashboard)
        
        # Circle screen
        circle = Screen(name='circle')
        circle.add_widget(CircleView())
        sm.add_widget(circle)
        
        # User screen
        info = Screen(name='info')
        info.add_widget(InfoScreen())
        sm.add_widget(info)
        
        # Settings screen
        settings = Screen(name='settings')
        settings.add_widget(Label(text='Settings Content'))
        sm.add_widget(settings)
        
    def show_screen(self, screen_name):
        self.ids.screen_manager.current = screen_name
    
    def select_button(self, button):
        if hasattr(self, 'selected_button') and self.selected_button:
            self.selected_button.state = 'normal'
        button.state = 'down'
        self.selected_button = button
            
    def return_to_registration(self):
        app = App.get_running_app()
        sm = app.root

        if self.previous_screen:
            sm.current = 'registration'
        else:
            print("Error: No previous screen to return to.")

    def on_kv_post(self, base_widget):
        if self.dashboard_button:
            self.select_button(self.dashboard_button)