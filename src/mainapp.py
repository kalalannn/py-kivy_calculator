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
from kivy.lang.builder import Builder
from kivy.factory import Factory

import re

KV = '''
#:kivy 1.8.0
#:import hex kivy.utils.get_color_from_hex
<MenuWidget@AnchorLayout>:
    anchor_x: 'right'
    OurButton:
        size_hint:(None, None)
        size: (100, 10)
        text: 'help'

<OurLabel@Label>:
    size: self.texture_size
    text_size: self.size
    halign: 'right'
    valign: 'middle'

<OurButton@Button>:
    background_color: hex('#026897')

<OurFunctionButton@Button>:
    background_color: hex('#026897')
    on_press: self.parent.parent.parent.operation(' ' + self.text + ' (')

<OurOperationButton@OurButton>:
    background_color: hex('#026897')
    on_press: self.parent.parent.parent.operation(self.text)

<OurNumberButton@Button>:
    background_color: hex('#cdeffe')
    on_press: self.parent.parent.parent.number(self.text)

MyWidget:
    canvas:
        Color: 
            rgba: hex('#03A9F4')
        Rectangle:
            size: self.size
            pos: self.pos

    orientation: 'vertical'
    padding: (5, 5, 5, 5)
    display: '0'

    MenuWidget:
        size_hint: (1, .05)

    OurLabel:
        text: root.display
        size_hint: (1, .2)
        color: 0,0,0
        canvas.before:
            Color: 
                rgba: hex('#e6f7fe')
            Rectangle:
                pos: self.pos[0], self.pos[1] + 10
                size: self.width, self.height - 15
        font_size: '34sp'

    BoxLayout:
        orientation: 'horizontal'
        size_hint: (1, .75)
        GridLayout:
            text1: 'log'
            text2: 'ln'
            rows: 7
            cols: 4
            OurButton:
                text: 'C'
                on_press: root.clear_display()
            OurFunctionButton:
                text: 'sqrt'
            OurFunctionButton:
                text: "power"
            OurButton:
                text: '<-'
                on_press: root.clear_symbol()
            OurButton:
                text: 'prev'
                on_press: self.parent.text1 = 'log' ; self.parent.text2 = 'ln'
            OurFunctionButton:
                id: first
                text: self.parent.text1
            OurFunctionButton:
                id: secound
                text: self.parent.text2
            OurButton:
                text: 'next'
                on_press: self.parent.text1 = 'fact' ; self.parent.text2 = 'nroot'
            OurNumberButton:
                text: '('
            OurNumberButton:
                text: ', '
            OurNumberButton:
                text: ')'
            OurOperationButton:
                text: '/'
            OurNumberButton:
                text: '7'
            OurNumberButton:
                text: '8'
            OurNumberButton:
                text: '9'
            OurOperationButton:
                text: '*'
            OurNumberButton:
                text: '4'
            OurNumberButton:
                text: '5'
            OurNumberButton:
                text: '6'
            OurOperationButton:
                text: '-'
            OurNumberButton:
                text: '1'
            OurNumberButton:
                text: '2'
            OurNumberButton:
                text: '3'
            OurOperationButton:
                text: '+'
            OurNumberButton:
                text: '0'
            OurNumberButton:
                text: '.'
            OurButton:
                text: "+/-"
                on_press: root.negate()
            OurButton:
                text: '='
                on_press: root.send()
'''


Window.size = (440, 400)

Config.set('graphics', 'resizeable', '1')

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if re.match(r'(^\d|numpad\d)', keycode[1]):
            self.number(keycode[1][-1])
        elif re.match(r'^[\+\-\*\/\.]', keycode[1]):
            self.operation (keycode[1][0])
        elif re.match(r'(\=|numpadenter|enter)', keycode[1]):
            self.send()
        elif re.match(r'^backspace', keycode[1]):
            self.clear_symbol()
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
        elif re.match(r'^\w$', keycode[1]):
            self.number(keycode[1])
        elif re.match(r'space', keycode[1]):
            self.number(' ')
        elif re.match(r'\,', keycode[1]):
            self.number(', ')

    def clear_display(self):
        self.display = '0';
    def clear_symbol(self):
        if len(self.display) == 1:
            self.display = '0'
        else:
            self.display = self.display[:-1]

    def operation(self, operation):
        if operation.count('(') != 0 and self.display == '0':
            self.display = ''
        self.display += operation;

    def number(self, number):
        if self.display == '0' and number != '.':
            self.display = number;
        else:
            self.display += number;
    def negate(self):
        if self.display[0] == '-':
            self.display = self.display[1:]
        else:
            self.display = '-' + self.display
    def send(self):
        print (self.display)

"""
    Main App class
"""
class CalculatorApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    Factory.register('MyWidget', cls=MyWidget)
    root = Builder.load_string(KV)
    CalculatorApp().run()
