from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import os
import base64
import yaml
from draw_input import DrawInput

class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super(ThirdWindow, self).__init__(**kwargs)
        layout = FloatLayout()

        self.painter = DrawInput()
        layout.add_widget(self.painter)

        title_label = Label(text="Sign Here", size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.9})
        layout.add_widget(title_label)

        clear_button = Button(text='Clear', size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'y': 0.05})
        clear_button.bind(on_release=self.clear_canvas)
        layout.add_widget(clear_button)

        save_button = Button(text='Save Data', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.05})
        save_button.bind(on_release=self.save_data)
        layout.add_widget(save_button)

        change_screen_button = Button(text='Back', size_hint=(0.2, 0.1), pos_hint={'x': 0.7, 'y': 0.05})
        change_screen_button.bind(on_release=self.change_screen)
        layout.add_widget(change_screen_button)

        self.add_widget(layout)

        self.nume = ""
        self.prenume = ""
        self.telefon = ""

    def update_inputs(self, nume, prenume, telefon):
        self.nume = nume
        self.prenume = prenume
        self.telefon = telefon

    def clear_canvas(self, instance):
        self.painter.clear_canvas()

    def save_data(self, instance):
        image_data = self.painter.get_image_data()
        self.save_to_yaml('data.yaml', image_data)

    def save_to_yaml(self, filename, image_data):
        path = os.getcwd()
        data = {
            'nume': self.nume,
            'prenume': self.prenume,
            'telefon': self.telefon,
            'signature': image_data
        }
        with open(f'{path}/{filename}', 'w') as file:
            yaml.dump(data, file)

    def change_screen(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'second'
