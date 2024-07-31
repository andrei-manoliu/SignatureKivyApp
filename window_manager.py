from kivy.uix.screenmanager import ScreenManager
from first_window import FirstWindow
from second_window import SecondWindow
from third_window import ThirdWindow

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.add_widget(FirstWindow(name='first'))
        self.add_widget(SecondWindow(name='second'))
        self.add_widget(ThirdWindow(name='third'))
