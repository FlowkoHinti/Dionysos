from numpy import array
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class Menu(StackLayout):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        self.username = TextInput(multiline=False)
        self.button = Button(text="OK")
        self.add_widget(Label(text='Name'))
        self.add_widget(self.username)
        self.add_widget(self.button)


class MyApp(App):

    def build(self):
        return Menu()


if __name__ == '__main__':
    MyApp().run()
