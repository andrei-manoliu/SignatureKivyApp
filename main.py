from kivy.app import App
from window_manager import WindowManager

class MobileApp(App):
    def build(self):
        sm = WindowManager()
        return sm

if __name__ == '__main__':
    MobileApp().run()
