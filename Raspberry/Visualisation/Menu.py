from numpy import array
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

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
                        on_press: root.start_game()
                    
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
            
        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"
            
'''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBue"

        return Builder.load_string(KV)

    def start_game(self):
        print("geht")

MainApp().run()
