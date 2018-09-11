from kivy.app import App
from kivy.app import Builder


class HellowWorld(App):
    def build(self):
        self.title = "Hello"
        self.root = Builder.load_file("widget.kv")
        return self.root

    def button_press(self):
        print("WHY?!")


HellowWorld().run()
