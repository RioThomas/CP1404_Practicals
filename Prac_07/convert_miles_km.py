"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers.
By Rio Thomas
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MI_TO_KM_CONVERSION_FACTOR = 1.609


class MilesToKilometersApp(App):
    """ MilesToKilometersApp is a Kivy App for converting Miles to Kilometers"""
    output = StringProperty()
    input = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 200)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        """Handle conversion, output result to output StringProperty."""
        try:
            value = int(value)
        except ValueError:
            value = 0
        result = value * MI_TO_KM_CONVERSION_FACTOR
        self.output = str(result)

    def handle_increment(self, increment):
        """Handle value incrementation, output result to input field via StringProperty."""
        try:
            self.input = self.root.ids.input_number.text
            self.input = str(int(self.input) + increment)
        except ValueError:
            self.input = str(increment)


MilesToKilometersApp().run()
