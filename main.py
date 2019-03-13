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
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#! Window.width = 500
Config.set('graphics', 'width', '500')

#! Window.height = 500
Config.set('graphics', 'height', '500')

#! Window.resizeable = False
Config.set('graphics', 'resizeable', '0')

"""
    We will change the design of this
"""
class OurSpecialButton(Button):
    def __init__(self, **kwargs):
        super(OurSpecialButton, self).__init__(**kwargs)

"""
    Fixed input buttons
"""
class InputButtonWidget(GridLayout):
    array = [
            'C', '/', "x\u00b3".format(), '<-',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '+/-', '=',
            ]
    rows = 5 
    cols = 4
    def __init__(self, **kwargs):
        super(InputButtonWidget, self).__init__(**kwargs)
        for x in self.array:
            self.add_widget(OurSpecialButton(text=x));

"""
    RootWidget class is a parent of all Widgets
"""
class RootWidget(BoxLayout):
    orientation = "vertical"
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(InputButtonWidget())

"""
    Main App class
"""
class CalculatorApp(App):
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    CalculatorApp().run()
