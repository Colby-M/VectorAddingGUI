
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from math import pi,cos,sin,atan,sqrt


class GUI(Widget):
    vectors = []

    def clearAll(self):
        self.ids.aInput.text = ''
        self.ids.mInput.text = ''
        self.ids.listVect.text = ''
        self.ids.errors.text = ''
        self.ids.totalAng.text = ''
        self.ids.totalMag.text = ''
        self.vectors.clear()
    def update(self):
        self.ids.listVect.text = str(self.vectors)
        self.ids.aInput.text = ''
        self.ids.mInput.text = ''
        self.ids.errors.text = ''

    def vect(self):
        if self.ids.aInput.text=='' or self.ids.mInput.text == '':
            self.ids.errors.text = 'Must input both an angle and magnitude'
        else:
            vector = (float(self.ids.mInput.text),  float(self.ids.aInput.text))
            self.vectors.append(vector)
            self.update()
        
    def addingVector(self):
        if not self.vectors:
            self.ids.errors.text = 'Must at least have inputted one vector'
        else:
            
            #constants and variables used
            DEG_CONVERT = pi / 180.0
            #Used to convert degrees to radians
            RAD_CONVERT = 180.0 / pi
            # Used to convert radians to degrees
            xsum = 0.0
            ysum = 0.0
            total = 0.0
            angle = 0.0
            types = (self.ids.angleButton.state != 'down')
            #end of variables
            for vector in self.vectors:
                if types == True:
                    xsum += vector[0] * cos(vector[1] * DEG_CONVERT)
                    ysum += vector[0] * sin(vector[1] * DEG_CONVERT)
                else:
                    xsum += vector[0] * cos(vector[1])
                    ysum += vector[0] * sin(vector[1])
            total = sqrt(xsum*xsum+ysum*ysum)
            total = round(total, 5)
            self.ids.totalMag.text = 'The final magnitude is: ' + str(total)
            if xsum != 0: # check for x = 0, if so, manually do angle
                angle = atan(ysum/xsum)
            else:
                angle = pi / 2 * ysum / abs(ysum)

            angle += (pi / 2) * (xsum < 0 and ysum > 0) # Q2 Shift
            angle += (pi * 1) * (xsum < 0 and ysum < 0) # Q3 shift
            angle += (pi * 2) * (xsum > 0 and ysum < 0) # Q4 shift

            angle = angle if types == False  else (angle * RAD_CONVERT)
            angle = round(angle, 5)
            self.ids.totalAng.text = 'The final angle of the vector is: ' + str(angle)
            self.vectors.clear()
            self.update()

class GUIApp(App):

    def build(self):
        return GUI()


if __name__ == '__main__':
    Window.maximize()
    GUIApp().run()
