from kivy.app import app
from game.guess_the_key import GuessTheKey

class GuessTheKeyApp(App):
    def build(self):
        return GuessTheKey()


if __name__ == "__main__":
    GuessTheKeyApp().run()
