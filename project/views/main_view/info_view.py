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

<CircleInfoLayout@BoxLayout>:
    is_mobile: False
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
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
            font_size: sp(20) if root.is_mobile else sp(30)
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
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Tensão normal minima: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Tensão de cisalhamento max: ±44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Posição do centro: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'Raio: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'θp: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
            ResponsiveLabel:
                is_mobile: root.is_mobile
                text: 'θc: 44.5'
                color: 1, 1, 1, 1
                size_hint_y: None
                height: dp(14) if root.is_mobile else dp(25)
                text_size: self.width, None
                halign: 'left'
            
<TableLayout@BoxLayout>:
    is_mobile: False
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20]

    BoxLayout:
        orientation: 'vertical' if root.is_mobile else 'horizontal'
        
        BoxLayout:
            size_hint: (1, 0.2) if root.is_mobile else (0.3, 1)          
            Label:
                text: 'Titulo'
                color: 1, 1, 1, 1
                font_size: sp(10) if root.is_mobile else sp(15)
                bold: True
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: (1, 0.8) if root.is_mobile else (0.7, 1)
            padding: [dp(10), dp(5)]
            spacing: dp(10)
            
            BoxLayout:
                size_hint_y: None
                height: dp(30)
                
                Label:
                    text: 'X'
                    color: 1, 1, 1, 1
                    bold: True
                    font_size: sp(10) if root.is_mobile else sp(15)
                Label:
                    text: 'Y'
                    color: 1, 1, 1, 1
                    bold: True
                    font_size: sp(10) if root.is_mobile else sp(15)
            
            BoxLayout:
                ResponsiveLabel:
                    is_mobile: root.is_mobile
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(10) if root.is_mobile else dp(25)
                ResponsiveLabel:
                    is_mobile: root.is_mobile
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(10) if root.is_mobile else dp(25)
            
            BoxLayout:
                ResponsiveLabel:
                    is_mobile: root.is_mobile
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(10) if root.is_mobile else dp(25)
                ResponsiveLabel:
                    is_mobile: root.is_mobile
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(10) if root.is_mobile else dp(25)

<InfoScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10) if root.is_mobile else dp(15)
        padding: [dp(10), dp(10)] if root.is_mobile else [dp(20), dp(20)]
        canvas.before:
            Color:
                rgba: utils.get_color_from_hex("#2A2E83")
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint_y: None
            height: dp(60) if root.is_mobile else dp(80)
            padding: [dp(10), dp(10)] if root.is_mobile else [dp(20), dp(20)]
            
            Label:
                text: 'Standard Information'
                font_size: sp(24) if root.is_mobile else sp(36)
                bold: True
                color: 1, 1, 1, 1
                size_hint_x: None
                width: self.texture_size[0]
                halign: 'left'
            
            Widget:
                size_hint_x: 1
            
            RoundedButton:
                text: 'Print'
                size_hint: None, None
                size: (dp(100), dp(40)) if root.is_mobile else (dp(150), dp(40))
                on_release: root.handle_print_infos()

        Label:
            text: 'Stresses, angles and positions'
            font_size: sp(18) if root.is_mobile else sp(24)
            color: 0.7, 0.7, 1, 1
            size_hint_y: None
            height: dp(30) if root.is_mobile else dp(40)
            halign: 'left'
            text_size: self.width, None
            padding: [dp(10), 0] if root.is_mobile else [dp(20), 0]
            
        Label:
            id: message_label
            text: root.message
            size_hint_y: 0.05
            height: dp(30)
            color: (0.9, 0.9, 1, 1) if root.message_type == 'success' else (1, 0.5, 0.5, 1)
            halign: 'center'
            valign: 'center'
            text_size: self.size

        BoxLayout:
            orientation: 'vertical' if root.is_mobile else 'horizontal'
            padding: [dp(10), 0, dp(10), dp(10)] if root.is_mobile else [dp(20), 0, dp(20), dp(20)]
            spacing: dp(20) if root.is_mobile else dp(150)
            
            CircleInfoLayout:
                is_mobile: root.is_mobile
                size_hint: (1, 0.4) if root.is_mobile else (0.3, 0.8)

            BoxLayout:
                orientation: 'vertical'
                size_hint: (1, 0.6) if root.is_mobile else (0.3, 0.8)
                spacing: dp(10) if root.is_mobile else dp(30)

                TableLayout:
                    is_mobile: root.is_mobile
                    size_hint_y: 1/3
                    height: dp(100) if root.is_mobile else dp(120)
                
                TableLayout:
                    is_mobile: root.is_mobile
                    size_hint_y: 1/3
                    height: dp(100) if root.is_mobile else dp(120)
                
                TableLayout:
                    is_mobile: root.is_mobile
                    size_hint_y: 1/3
                    height: dp(100) if root.is_mobile else dp(120)
''')

class InfoScreen(Screen):
    message = StringProperty('')
    message_type = StringProperty('success')
    is_mobile = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
        Window.bind(size=self.check_window_size)
        self.check_window_size()
    
    def check_window_size(self, *args):
        self.is_mobile = Window.width < dp(600)
    
    def handle_print_infos(self):
        try:
            # Add the function to print infos
            self.message = "Print performed successfully!"
            self.message_type = 'success'
        except:
            self.message = "Error: Please enter a valid integer for the angle."
            self.message_type = 'error'
        
        Clock.schedule_once(self.clear_message, 5)
    
    def clear_message(self, dt):
        self.message = ''
        self.message_type = 'success'