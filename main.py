from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class main (App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1



if __name__ == '__main__':
    main().run()