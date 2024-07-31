from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        layout = FloatLayout()

        self.nume_input = TextInput(hint_text='Nume', size_hint=(0.6, 0.1), pos_hint={'x': 0.2, 'y': 0.7})
        self.prenume_input = TextInput(hint_text='Prenume', size_hint=(0.6, 0.1), pos_hint={'x': 0.2, 'y': 0.55})
        self.telefon_input = TextInput(hint_text='Telefon', size_hint=(0.6, 0.1), pos_hint={'x': 0.2, 'y': 0.4})
        layout.add_widget(self.nume_input)
        layout.add_widget(self.prenume_input)
        layout.add_widget(self.telefon_input)

        sign_button = Button(text='Sign', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.05})
        sign_button.bind(on_release=self.go_to_third)
        layout.add_widget(sign_button)

        back_button = Button(text='Back', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.2})
        back_button.bind(on_release=self.go_to_first)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_third(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'third'
        self.manager.get_screen('third').update_inputs(self.nume_input.text, self.prenume_input.text, self.telefon_input.text)

    def go_to_first(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'first'
