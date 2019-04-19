"""
    MainApp
    Documentation for kivy: https://kivy.org/doc/stable/api-kivy.html
"""

##  
#   @file main.py
#   @author Nikolaj Vorobiev
#   @date 13.03
#   @brief MainApplication file
#   Will be updated 

from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import re

#! Window.width = 500
Config.set('graphics', 'width', '500')

#! Window.height = 500
Config.set('graphics', 'height', '500')

#! Window.resizeable = False
Config.set('graphics', 'resizeable', '0')


class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        #key = re.sub(r'^numpad(\d|add|substract|mul|divide)', keycode[1], '\1')
        print(keycode[1])
        if re.match(r'(^\d|numpad\d)', keycode[1]):
            self.number(keycode[1][-1])
        elif re.match(r'^[\+\-\*\/\.]', keycode[1]):
            self.operation (keycode[1][0])
        elif re.match(r'(\=|numpadenter|enter)', keycode[1]):
            self.send()
        elif re.match(r'^numpad.*', keycode[1]):
            if keycode[1][6:] == 'add':
                self.operation('+')
            elif keycode[1][6:] == 'substract':
                self.operation('-')
            elif keycode[1][6:] == 'mul':
                self.operation('*')
            elif keycode[1][6:] == 'divide':
                self.operation('/')
            elif keycode[1][6:] == 'decimal':
                self.operation('.')
        return True

    def clear_display(self):
        self.display = '0';
    def clear_symbol(self):
        if len(self.display) == 1:
            self.display = '0'
        else:
            self.display = self.display[:-1]

    def operation(self, operation):
        self.display += operation;

    def number(self, number):
        if self.display == '0':
            self.display = number;
        else:
            self.display += number;

    def negate(self):
        if self.display[0] == '-':
            self.display = self.display[1:]
        elif re.match(r'^[^0]+', self.display[0]):
            self.display = '-' + self.display
    def send(self):
        print (self.display)


"""
    Main App class
"""
class CalculatorApp(App):
    pass

    """
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)
    def build(self):
        return RootWidget()
    """

if __name__ == '__main__':
    CalculatorApp().run()
