import kivy

from kivy.app import App
from kivy.uix.label import Label

class aplicacion(App):
    def build(self):
        return Label(text='Bienvenido rama puto')
    
    
if __name__ == '__main__':
    aplicacion().run()