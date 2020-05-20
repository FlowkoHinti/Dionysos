from kivymd.app import MDApp
from kivy.lang import Builder
from subprocess import call

KV = '''
BoxLayout:
    orientation: "vertical"
    
    MDToolbar:
        title: "DIONYSOS"
        halign: "center"
        
    GridLayout:
        cols: 3
        spacing: 10, 10
        
        
        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"
            
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    text: "Tetris"
                    theme_text_color: "Primary"
                    halign: "center"
                
                Image:
                    source: "A:/Dionysos/tetris.jpg"
                    allow_stretch: True
                    keep_ratio: False
                
                BoxLayout:
                    
                    MDRectangleFlatIconButton:
                        icon: "play"
                        text: "Play"
                        width: dp(140)
                        on_press: app.start_game('t')
                    
                    MDRectangleFlatIconButton:
                        icon: "trophy"
                        text: "Highscore"
                        width: dp(140)

        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"

            
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    text: "Snake"
                    theme_text_color: "Primary"
                    halign: "center"
                
                Image:
                    source: "A:/Dionysos/tetris.jpg"
                    allow_stretch: True
                    keep_ratio: False
                
                BoxLayout:
                    
                    MDRectangleFlatIconButton:
                        icon: "play"
                        text: "Play"
                        width: dp(140)
                        on_press: app.start_game('s')
                    
                    MDRectangleFlatIconButton:
                        icon: "trophy"
                        text: "Highscore"
                        width: dp(140)
            
        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"
            
        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"
                
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
