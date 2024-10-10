from kivy.lang import Builder
from kivy.utils import get_color_from_hex

# Color definitions
colors = {
    'primary': get_color_from_hex('#2C3E99'),
    'secondary': get_color_from_hex('#4169E1'),
    'background': get_color_from_hex('#2A2E83'),
    'light': get_color_from_hex('#2C3E99'),
    'text_light': get_color_from_hex('#f2f1f1'),
    'text_dark': get_color_from_hex('#7D7D7D'),
    'hover': get_color_from_hex('#3B48C2'),
    'button_hover': get_color_from_hex('#1c86e2'),
    'sidebar': get_color_from_hex('#4169E1'),
    'return_button': get_color_from_hex('#4C5CD2')
}

# Style definitions
styles = '''
<CardWidget@BoxLayout>:
    canvas.before:
        Color:
            rgba: app.colors['primary']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]
    padding: 40
    spacing: 20

<StylizedButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ''
    color: app.colors['text_dark']
    font_size: '16sp'
    bold: True
    size_hint: None, None
    size: 200, 50
    canvas.before:
        Color:
            rgba: app.colors['light'] if self.state == 'normal' else app.colors['button_hover']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]

<StylizedTextInput@TextInput>:
    background_color: app.colors['light']
    foreground_color: 0, 0, 0, 1
    size_hint: None, None
    size: 250, 40
    multiline: False
    padding: [10, 10, 10, 10]
    font_size: '16sp'
    halign: 'center'
    canvas.before:
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)
            width: 2
    
<StylizedLabel@Label>:
    color: app.colors['text_light']
    font_size: '20sp'
    font_name: 'Arial'

<TitleLabel@Label>:
    color: app.colors['text_light']
    font_size: '30sp'
    font_name: 'Arial'
    bold: True

<MenuButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint_y: None
    height: 50
    text_size: self.size
    halign: 'left'
    valign: 'center'
    padding: [20, 0]
    font_size: '16sp'
    canvas.before:
        Color:
            rgba: (*app.colors['hover'][:3], 0.4) if self.state == 'down' else (0, 0, 0, 0)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<Sidebar@BoxLayout>:
    canvas.before:
        Color:
            rgba: app.colors['sidebar']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20, 0, 0, 20]
    orientation: 'vertical'
    padding: 20
    spacing: 10

<ContentArea@BoxLayout>:
    canvas.before:
        Color:
            rgba: app.colors['background']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [0, 20, 20, 0]

<ReturnButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint_y: None
    height: 50
    canvas.before:
        Color:
            rgba: app.colors['return_button']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8,]

<NavigationButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint: None, None
    size: 50, 50
    font_size: '24sp'
    canvas.before:
        Color:
            rgba: app.colors['background'] if self.state == 'normal' else app.colors['hover']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5,]
'''

def load_styles():
    Builder.load_string(styles)