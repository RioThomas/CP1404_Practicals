"""
CP1404 Practical
Kivy GUI program to convert generate labels.
By Rio Thomas
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """DynamicLabelApp is a demo Kivy App for generating labels using python."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_name_list = ('1', '2', '3', '4')

    def build(self):
        self.title = "Label Generator"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.generate_labels()
        return self.root

    def generate_labels(self):
        for variable in self.label_name_list:
            temp_label = Label(text=variable, id=variable)
            self.root.ids.output_div.add_widget(temp_label)


DynamicLabelApp().run()
