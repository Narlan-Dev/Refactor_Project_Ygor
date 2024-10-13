from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from views.main_view.circle_view import CircleView
from views.main_view.info_view import InfoScreen
from views.main_view.rotation_angle_view import RotationAngleScreen
from views.main_view.settings_view import SettingsScreen
from styles import colors
from kivy.metrics import dp
from kivy.core.window import Window

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
            radius: [dp(10),]

<RoundedLabel@Label>:
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),]
            
<RoundedTextInput@TextInput>:
    background_color: 0, 0, 0, 0
    cursor_color: 1, 1, 1, 1
    foreground_color: 1, 1, 1, 1
    hint_text_color: 1, 1, 1, 0.7 
    selection_color: 0.22, 0.33, 0.7, 0.5 
    padding: [dp(10), dp(10)]
    size_hint: None, None
    size: dp(150), dp(40)
    multiline: False
    halign: 'center'
    valign: 'middle'

<MenuButton@Button>:
    background_color: 0, 0, 0, 0
    color: 1, 1, 1, 1  # White text color
    font_size: sp(14)
    size_hint_y: None
    height: dp(50)
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    padding_x: dp(10)
    icon_source: ''
    is_mobile: False
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1") if self.state == "normal" else utils.get_color_from_hex("#3A5FCC")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),]
    Image:
        source: root.icon_source
        center_x: root.center_x
        center_y: root.center_y
        size: dp(24), dp(24)
        opacity: 1 if root.is_mobile else 0

<MainWindow>:
    circle_button: circle_button
    info_button: info_button
    rotation_button: rotation_button
    settings_button: settings_button

    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#2A2E83")
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: 'vertical' if root.is_mobile else 'horizontal'
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
                    radius: [0, 0, dp(20), dp(20)] if root.is_mobile else [0, dp(20), dp(20), 0]
            
            orientation: 'horizontal' if root.is_mobile else 'vertical'
            size_hint: (1, None) if root.is_mobile else (None, 1)
            height: dp(80) if root.is_mobile else self.parent.height
            width: self.parent.width if root.is_mobile else min(dp(250), 0.25 * root.width)
            padding: dp(10)
            spacing: dp(5)

            Label:
                text: 'Menu'
                font_size: sp(20) if root.is_mobile else sp(24)
                size_hint: (None, 1) if root.is_mobile else (1, None)
                width: dp(80) if root.is_mobile else self.parent.width
                height: dp(50) if not root.is_mobile else self.parent.height
                bold: True

            # MenuButtons
            BoxLayout:
                orientation: 'horizontal' if root.is_mobile else 'vertical'
                size_hint: (1, 1) if root.is_mobile else (1, None)
                height: self.minimum_height if not root.is_mobile else self.parent.height
                spacing: dp(5)
                
                    
                MenuButton:
                    id: circle_button
                    text: root.circle_text
                    icon_source: root.circle_icon
                    is_mobile: root.is_mobile
                    on_release: 
                        root.show_screen('circle')
                        root.select_button(self)

                MenuButton:
                    id: info_button
                    text: root.info_text
                    icon_source: root.info_icon
                    is_mobile: root.is_mobile
                    on_release: 
                        root.show_screen('info')
                        root.select_button(self)

                MenuButton:
                    id: rotation_button
                    text: root.rotation_text
                    icon_source: root.rotation_icon
                    is_mobile: root.is_mobile
                    on_release: 
                        root.show_screen('rotation')
                        root.select_button(self)
                        
                MenuButton:
                    id: settings_button
                    text: root.settings_text
                    icon_source: root.settings_icon
                    is_mobile: root.is_mobile
                    on_release: 
                        root.show_screen('settings')
                        root.select_button(self)
                
            Widget:
                # Spacer
                size_hint_x: None if root.is_mobile else 1
                width: dp(10) if root.is_mobile else self.parent.width

            Button:
                text: 'Return'
                size_hint: (None, 1) if root.is_mobile else (1, None)
                width: dp(80) if root.is_mobile else self.parent.width
                height: dp(50) if not root.is_mobile else self.parent.height
                background_color: 0, 0, 0, 0
                color: 1, 1, 1, 1
                on_release: root.return_to_registration()
                canvas.before:
                    Color:
                        rgba: 0.298, 0.361, 0.824, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10), ]
                
        # Content Area
        ScreenManager:
            id: screen_manager
            canvas.before:
                Color:
                    rgba: utils.get_color_from_hex("#2A2E83")
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(20), dp(20), 0, 0] if root.is_mobile else [0, dp(20), dp(20), 0]
''')

class MainWindow(BoxLayout):
    circle_button = ObjectProperty(None)
    info_button = ObjectProperty(None)
    rotation_button = ObjectProperty(None)
    settings_button = ObjectProperty(None)
    is_mobile = BooleanProperty(False)
    
    circle_text = StringProperty('Circle Mohr')
    info_text = StringProperty('Info')
    rotation_text = StringProperty('Rotate')
    settings_text = StringProperty('Settings')

    circle_icon = StringProperty('icons/qualquer.png')
    info_icon = StringProperty('icons/qualquer.png')
    rotation_icon = StringProperty('icons/qualquer.png')
    settings_icon = StringProperty('icons/qualquer.png')

    def __init__(self, sigma_x=None, sigma_y=None, txy=None, previous_screen=None, **kwargs):
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        self.txy = txy
        self.previous_screen = previous_screen
        self.selected_button = None
        super().__init__(**kwargs)
        
        # Initialize screens
        self.init_screens()
        
        # Bind to window size changes
        Window.bind(size=self.check_window_size)
        
        # Initial check
        self.check_window_size()
        
    def check_window_size(self, *args):
        # Consider it mobile if the width is less than 600dp
        self.is_mobile = Window.width < dp(600)
        self.update_button_texts()

    def update_button_texts(self):
        if self.is_mobile:
            self.circle_text = ''
            self.info_text = ''
            self.rotation_text = ''
            self.settings_text = ''
        else:
            self.circle_text = 'Circle Mohr'
            self.info_text = 'Info'
            self.rotation_text = 'Rotate'
            self.settings_text = 'Settings'

    def init_screens(self):
        sm = self.ids.screen_manager
        
        
        # Circle screen
        circle = Screen(name='circle')
        circle.add_widget(CircleView())
        sm.add_widget(circle)
        
        # Info screen
        info = Screen(name='info')
        info.add_widget(InfoScreen())
        sm.add_widget(info)
        
        # Rotation screen
        rotation = RotationAngleScreen(name='rotation')
        rotation.update_information(self.sigma_x, self.sigma_y, self.txy)
        sm.add_widget(rotation)
        
        # Settings screen
        settings = Screen(name='settings')
        settings.add_widget(SettingsScreen())
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
        if self.circle_button:
            self.select_button(self.circle_button)