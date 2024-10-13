from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

Builder.load_string('''
#:import utils kivy.utils

<ResponsiveLabel@Label>:
    is_mobile: False
    font_size: self.height * 1 if self.is_mobile else self.height * 0.6

<SettingsLayout@BoxLayout>:
    is_mobile: False
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#2A2E83")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20]
    
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(70) if root.is_mobile else dp(80)
        
        Label:
            text: 'Informações do círculo'
            color: 1, 1, 1, 1
            font_size: sp(30) if root.is_mobile else sp(30)
            bold: True
            size_hint_y: None
            height: dp(50) if root.is_mobile else dp(60)
            padding: [dp(15), 0]
        
        Widget:
            size_hint_y: None
            height: dp(1)
            canvas:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.x + dp(15), self.y
                    size: self.width - dp(30), 1
    
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: [dp(15), dp(10)]
            spacing: dp(10) if root.is_mobile else dp(20)
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Tensão normal maxima: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Tensão normal minima: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Tensão de cisalhamento max: ±44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Posição do centro: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Raio: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'θp: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'θc: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(20) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'

<SettingsScreen>:        
    SettingsLayout:
        is_mobile: root.is_mobile
        size_hint: (1, 1) if root.is_mobile else (1, 1)
''')

class SettingsScreen(Screen):
    is_mobile = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        Window.bind(size=self.check_window_size)
        self.check_window_size()
    
    def check_window_size(self, *args):
        self.is_mobile = Window.width < dp(600)