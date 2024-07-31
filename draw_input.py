from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
import os
import base64

class DrawInput(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 1)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()

    def get_image_data(self):
        # Save the canvas as an image and read the image data as base64
        path = os.path.join(os.getcwd(), 'signature.png')
        self.export_to_png(path)
        with open(path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
