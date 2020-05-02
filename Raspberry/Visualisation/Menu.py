from numpy import array
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import Screen
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
            
            MDLabel:
                text: "Tetris"
                theme_text_color: "Primary"
                halign: "center"
                
        
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
        self.theme_cls.primary_palette = "LightBlue"
        """screen = Screen()

        screen.add_widget(
            MDToolbar(title="DIONYSOS", type="top")
        )
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        screen.add_widget(
            MDRectangleFlatButton(
                text="Test",
                pos_hint={"center_x": 0.2, "center_y": 0.5},
            )
        )"""

        return Builder.load_string(KV)


MainApp().run()
