from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from views.registration_form import RegistrationForm
from views.main_view.main_window import MainWindow
from styles import colors, load_styles

class MohrCircleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = colors

    def build(self):
        Window.size = (1280, 720)
        load_styles()

        # Initialize the ScreenManager
        sm = ScreenManager()

        # Create and add the RegistrationForm screen
        registration_screen = Screen(name='registration')
        registration_screen.add_widget(RegistrationForm())

        # Create and add the MainWindow screen
        main_screen = Screen(name='main')
        main_screen.add_widget(MainWindow())  # Keep MainWindow empty initially

        # Add screens to the ScreenManager
        sm.add_widget(registration_screen)
        sm.add_widget(main_screen)

        return sm

if __name__ == "__main__":
    MohrCircleApp().run()
