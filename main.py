import sys
sys.path.insert(0, "/usr/local/lib/python3.7/site-packages")
from kivy.app import App
from game.guess_the_key import GuessTheKey

class GuessTheKeyApp(App):
    def build(self):
        return GuessTheKey()


if __name__ == "__main__":
    GuessTheKeyApp().run()
