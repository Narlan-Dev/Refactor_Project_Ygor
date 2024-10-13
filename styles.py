from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

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
            rgba: app.colors['sidebar']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(20),]
    padding: dp(20)
    spacing: dp(10)

<StylizedButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ''
    color: app.colors['text_light']
    font_size: sp(14)
    bold: True
    size_hint: None, None
    size: min(dp(200), 0.8 * self.parent.width), dp(50)
    canvas.before:
        Color:
            rgba: app.colors['return_button'] if self.state == 'normal' else app.colors['button_hover']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(15),]

<StylizedTextInput@TextInput>:
    background_color: 0, 0, 0, 0 #app.colors['light']
    foreground_color: 0, 0, 0, 1
    size_hint: None, None
    size: min(dp(250), 0.8 * self.parent.width), dp(40)
    multiline: False
    padding: [dp(10), dp(10), dp(10), dp(10)]
    font_size: sp(14)
    halign: 'center'
    canvas.before:
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, dp(10))
            width: 2
    
<StylizedLabel@Label>:
    color: app.colors['text_light']
    font_size: sp(16)
    font_name: 'Arial'
    text_size: self.width, None
    size_hint: 1, None
    height: self.texture_size[1]

<TitleLabel@Label>:
    color: app.colors['text_light']
    font_size: sp(24)
    font_name: 'Arial'
    bold: True
    text_size: self.width, None
    size_hint: 1, None
    height: self.texture_size[1]

<MenuButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint_y: None
    height: dp(50)
    text_size: self.width, None
    halign: 'left'
    valign: 'center'
    padding: [dp(20), 0]
    font_size: sp(14)
    canvas.before:
        Color:
            rgba: (*app.colors['hover'][:3], 0.4) if self.state == 'down' else (0, 0, 0, 0)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10),]

<Sidebar@BoxLayout>:
    canvas.before:
        Color:
            rgba: app.colors['sidebar']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(20), 0, 0, dp(20)]
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(5)

<ContentArea@BoxLayout>:
    canvas.before:
        Color:
            rgba: app.colors['background']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [0, dp(20), dp(20), 0]

<ReturnButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint_y: None
    height: dp(50)
    font_size: sp(14)
    canvas.before:
        Color:
            rgba: app.colors['return_button']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8),]

<NavigationButton@Button>:
    background_color: 0, 0, 0, 0
    color: app.colors['text_light']
    size_hint: None, None
    size: dp(50), dp(50)
    font_size: sp(20)
    canvas.before:
        Color:
            rgba: app.colors['background'] if self.state == 'normal' else app.colors['hover']
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(5),]
'''

def load_styles():
    Builder.load_string(styles)