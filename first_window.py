from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super(FirstWindow, self).__init__(**kwargs)
        layout = FloatLayout()

        button = Button(text='Personal Information', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.45})
        button.bind(on_release=self.change_screen)
        layout.add_widget(button)

        self.add_widget(layout)

    def change_screen(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'second'
