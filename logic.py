from kivy.config import Config

#-------- Setting Up the dimensions ----------------------
Config.set('graphics','resizable',0)

Config.set('graphics','width','500')

Config.set('graphics','height','700')

#-----------Main Program -----------------------------------

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.uix.button import Button



class MainScreen(Screen):
    label_text = StringProperty("0")
    answer_text = StringProperty()
    ops = ["+","/","*","-"]
    
    

    def delete(self,widget):
        self.label_text = self.label_text[:-1]


    def pressed(self,widget):
        if "+" in self.ops or "-" in self.ops or "*" in self.ops or "/" in self.ops:
            try:
                self.answer_text = str(eval(self.label_text))
            except Exception:
                self.answer_text = ""
                

        if self.label_text == "0":
            self.label_text = widget.text
            
        else:
            self.label_text += widget.text

        try:
            
            self.answer_text = str(eval(self.label_text))
            self.label_text = self.label_text

        except Exception:

            self.answer_text = ""


    def drg(self,widget):
        pass


    def clear(self,widget):
        self.label_text = "0"
        self.answer_text = ""
       

    
    def ans(self,widget):
        pass


    def equals(self,widget):
        try:
            self.answer_text = str(eval(self.label_text))
            self.label_text = str(eval(self.label_text))
            

        except SyntaxError:
            self.label_text = '0'
            self.answer_text = 'Syntax Error'
            


    def operation(self,widget):
        try:
            self.answer_text = str(eval(self.label_text))
            self.label_text += widget.text
        except Exception:
            self.label_text += widget.text
            self.answer_text = self.answer_text

    def brackets(self,widget):
        if widget.text == "(":
            self.label_text += widget.text
            
        else:
            self.label_text += widget.text
            
# --------- Button Classes -----------------------------------------------------------------         

class NumberButton(Button):
    background_color_number = "#9d9cb5"
    foreground_color_number = "#e2e1e8"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = self.background_color_number
        #self.background_normal = ''
        self.color = self.foreground_color_number
        self.bold = True
        
class OperationButton(Button):
    background_color_number = "#d49a1e"
    foreground_color_number = "#eae9e5"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = self.background_color_number
        #self.background_normal = ''
        self.color = self.foreground_color_number
        self.bold = True

class FunctionButton(Button):
    background_color_number = "#66c1f3"
    foreground_color_number = "#f7f5f1"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = self.background_color_number
        #self.background_normal = ''
        self.color = self.foreground_color_number
        self.bold = True

#------------------------------------------------------------------------------------------------

#----------------Main App Class ----------------------------------------------------------------

class CalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="mainscreen"))
        return sm
    
# ------------------------------------------------------------------------------------------------



if __name__ == "__main__":
    CalculatorApp().run()