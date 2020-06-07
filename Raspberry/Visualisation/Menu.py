from kivy.config import Config

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)
Config.write()

from kivy.core.window import Window

Window.size = (800, 480)

from kivymd.app import MDApp
from kivy.lang import Builder
from subprocess import call

# 800x480
# 110mmx66mm

KV = '''
BoxLayout:
    orientation: "vertical"
    
    MDCard:
        size_hint: 1, None
        md_bg_color: [0,0,0,0]
        FloatLayout:
            pos: self.parent.pos
            Image:
                pos: self.parent.pos
                source:"icons/grape.png"
            MDLabel:
                halign: "center"
                pos: self.parent.pos
                markup: True
                theme_text_color: "Custom"
                outline_width: dp(2)
                outline_color: [1,0.8,0]
                text: "[b][i][size=35][color=#303030]DIONYSOS[/color][/size][/i][/b]"

           
          
            
                        
    
    GridLayout:
        cols: 3
        spacing: 10, 10
        
        MDCard:
            size_hint: None, None
            size: "395dp", "253dp"
            background: "icons/tetris.jpg"
            
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    markup: True
                    theme_text_color: "Custom"
                    outline_width: dp(2)
                    outline_color: [1,0.8,0]
                    text: "[b][size=50][color=#FF0000]T[/color][color=#FFA000]E[/color][color=#FFE000]T[/color][color=#00E000]R[/color][color=#00DFFF]I[/color][color=#AF00FF]S[/color][/size][/b]"
                    halign: "center"
                
                
                BoxLayout:
                    
                    MDRectangleFlatIconButton:
                        icon: "play"
                        markup: True
                        text: "[b][size=20]Play[/size][/b]"
                        height: dp(50)
                        width: dp(197)
                        on_press: app.start_game('t')
                    
                    MDRectangleFlatIconButton:
                        icon: "trophy"
                        markup: True
                        text: "[b][size=20]Highscore[/size][/b]"
                        height: dp(50)
                        width: dp(197)

        MDCard:
            size_hint: None, None
            size: "395dp", "253dp"
            background: "icons/snake.jpg"
            
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    theme_text_color: "Custom"
                    markup: True
                    outline_width: dp(2)
                    outline_color: [1,0.8,0]
                    text: "[b][size=50][color=#00FF00]S[/color][color=#00FF00]N[/color][color=#00FF00]A[/color][color=#00FF00]K[/color][color=#FF0000]E[/color][/size][/b]"
                    halign: "center"
                
                
                BoxLayout:
                    
                    MDRectangleFlatIconButton:
                        icon: "play"
                        markup: True
                        text: "[b][size=20]Play[/size][/b]"
                        height: dp(50)
                        width: dp(197)
                        on_press: app.start_game('t')
                    
                    MDRectangleFlatIconButton:
                        icon: "trophy"
                        markup: True
                        text: "[b][size=20]Highscore[/size][/b]"
                        height: dp(50)
                        width: dp(197)
        
'''


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_string(KV)

    def start_game(self, game):
        if game == 't':
            call('Tetris.py', shell=True)
        elif game == 's':
            call('Snake.py', shell=True)


MainApp().run()
