from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

Builder.load_string('''
<CircleInfoLayout@BoxLayout>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20]
    
    # Title with bottom border
    BoxLayout:
        size_hint_y: None
        height: 60
        canvas.after:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.x + 15, self.y
                size: self.width - 30, 1
        
        Label:
            text: 'Informações do círculo'
            color: 1, 1, 1, 1
            font_size: '30sp'
            bold: True
            padding: [15, 0]
    
    # Info content
    BoxLayout:
        orientation: 'vertical'
        padding: [15, 10, 15, 10]
        spacing: 20
        
        Label:
            text: 'Tensão normal maxima: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'Tensão normal minima: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'Tensão de cisalhamento max: ±44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'Posição do centro: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'Raio: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'θp: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
        Label:
            text: 'θc: 44.5'
            color: 1, 1, 1, 1
            size_hint_y: None
            height: 25
            text_size: self.size
            font_size: '20sp'
            halign: 'left'
            
<TableLayout@BoxLayout>:
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#4169E1")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20]

    BoxLayout:
        orientation: 'horizontal'
        
        # Left side - Title with right border
        BoxLayout:
            size_hint_x: 0.3
            canvas.after:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.right, self.y + 10
                    size: 1, self.height - 20
            
            Label:
                text: 'Titulo'
                color: 1, 1, 1, 1
                font_size: '24sp'
                bold: True
        
        # Right side - X/Y columns
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.7
            padding: [10, 5]
            spacing: 5
            
            # Headers
            BoxLayout:
                size_hint_y: None
                height: 30
                
                Label:
                    text: 'X'
                    color: 1, 1, 1, 1
                    bold: True
                    font_size: '20sp'
                Label:
                    text: 'Y'
                    color: 1, 1, 1, 1
                    bold: True
                    font_size: '20sp'
            
            # First row
            BoxLayout:
                Label:
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                Label:
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
            
            # Second row
            BoxLayout:
                Label:
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1
                Label:
                    text: 'θp: 44.5'
                    color: 1, 1, 1, 1

<InfoScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 15
        padding: [20, 20]
        canvas.before:
            Color:
                rgba: utils.get_color_from_hex("#2A2E83")
            Rectangle:
                pos: self.pos
                size: self.size

        # Header area
        BoxLayout:
            size_hint_y: None
            height: 
            padding: [20, 20, 20, 20]
            
            Label:
                text: 'Standard Information'
                font_size: '36sp'
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
                size: 150, 40
                on_release: root.handle_print_infos()

        # Sub Title
        Label:
            text: 'Stresses, angles and positions'
            font_size: '24sp'
            color: 0.7, 0.7, 1, 1
            size_hint_y: None
            height: 5
            halign: 'left'
            text_size: self.width, None
            padding: [20, 0, 20, 20]
            
        # Message
        Label:
            id: message_label
            text: root.message
            size_hint_y: 0.05
            height: 30
            color: (0.9, 0.9, 1, 1) if root.message_type == 'success' else (1, 0.5, 0.5, 1)
            halign: 'center'
            valign: 'center'
            text_size: self.size

        # Main content
        BoxLayout:
            padding: [20, 0, 20, 20]
            spacing: 150
            
            # Left panel - Circle Information
            CircleInfoLayout:
                size_hint: 0.3, 0.8

            # Right panel - Tables
            BoxLayout:
                orientation: 'vertical'
                size_hint: 0.3, 0.8
                spacing: 30

                TableLayout:
                    size_hint_y: 1/3
                    height: 120
                
                TableLayout:
                    size_hint_y: 1/3
                    height: 120
                
                TableLayout:
                    size_hint_y: 1/3
                    height: 120
''')

class InfoScreen(Screen):
    message = StringProperty('')
    message_type = StringProperty('success')

    def __init__(self, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
    
    def handle_print_infos(self):
        try:
            # Add the function to print infos
            self.message = "Print performed successfully!"
            self.message_type = 'success'
        except:
            self.message = "Error: Please enter a valid integer for the angle."
            self.message_type = 'error'
        pass
    
        Clock.schedule_once(self.clear_message, 5)
    
    def clear_message(self, dt):
        self.message = ''
        self.message_type = 'success'