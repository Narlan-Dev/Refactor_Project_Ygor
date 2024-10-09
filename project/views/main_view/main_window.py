from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from views.main_view.circle_view import CircleView
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

<MainWindow>:
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
                    radius: [20, 0, 0, 20]
            
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

            MenuButton:
                text: 'Dashboard'
                on_release: root.show_screen('dashboard')
                
            MenuButton:
                text: 'Circle Mohr'
                on_release: root.show_screen('circle')
                
            MenuButton:
                text: 'User'
                on_release: root.show_screen('user')
                
            MenuButton:
                text: 'Settings'
                on_release: root.show_screen('settings')
                
            Widget:
                # Spacer
                
            Button:
                text: 'Return'
                size_hint_y: None
                height: 50
                background_color: 0.298, 0.361, 0.824, 0.6
                on_release: root.return_to_registration()
                
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
    def __init__(self, sigma_x=None, sigma_y=None, txy=None, previous_screen=None, **kwargs):
        super().__init__(**kwargs)
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        self.txy = txy
        self.previous_screen = previous_screen
        
        # Initialize screens
        self.init_screens()
        
    def init_screens(self):
        sm = self.ids.screen_manager
        
        # Dashboard screen
        dashboard = DashboardScreen(name='dashboard')
        sm.add_widget(dashboard)
        
        # Circle screen
        circle = Screen(name='circle')
        circle.add_widget(CircleView())
        sm.add_widget(circle)
        
        # User screen
        user = Screen(name='user')
        user.add_widget(Label(text='User Profile Content'))
        sm.add_widget(user)
        
        # Settings screen
        settings = Screen(name='settings')
        settings.add_widget(Label(text='Settings Content'))
        sm.add_widget(settings)
        
    def show_screen(self, screen_name):
        self.ids.screen_manager.current = screen_name
        
    def return_to_registration(self):
        app = App.get_running_app()
        sm = app.root

        if self.previous_screen:
            sm.current = 'registration'
        else:
            print("Error: No previous screen to return to.")