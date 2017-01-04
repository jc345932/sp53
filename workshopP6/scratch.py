from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class ConvertNumberApp(App):
    def build(self):
        Window.size = (1000, 750)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('scratch.kv')
        return self.root
    def handle_calculate(self):
        value = self.get_validNumber()
        result = value *1.60934
        self.root.ids.output_label.text = str(result)
    def handle_valueChange(self, change):
        value = self.get_validNumber() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()
    def get_validNumber(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertNumberApp().run()










