#Unit Conversion Prog
#Jonathan Harris, August 5, 2014
#This is a unit conversion program using my own conversion library

import os
import platform
from alpha import Temperature
from Tkinter import *
from ttk import *

img = None

#This creates the main menu for the program
class Menus:

    def __init__(self, root):
        self.root = root
        self.mainM()
        if os.name == 'nt':
            self.root.iconbitmap("icons\image.ico")
        elif os.name == 'posix':
            if platform.system() == 'Linux':
                img = PhotoImage(file = "icons\image.png")
                self.root.call('wm', 'iconphoto', self.root._w, img)
            elif platform.system() == 'Darwin':
                img = PhotoImage(file = "icons\image.icns")
                self.root.call('wm', 'iconphoto', self.root._w, imgs)


#This is the Main Menu
    def mainM(self):
        self.frame = Frame(self.root)
        self.frame.grid(column = 0, row = 0, sticky = (N,S,E,W))
        self.root.title("Unit Converter")

        self.butlabs = ['Temperature', 'Length', 'volume', 'Pressure',
                        'Speed', 'Energy', 'N/A', 'N/A']

        self.varCol = 0
        self.newrow = False

        for word in self.butlabs:
            self.varCol +=1

            if word == 'Temperature':
                self.options = Button(self.frame, text = word,
                 command  = self.temperM)
            else:
                self.options = Button(self.frame, text = word, command = None)
            if word == 'Temperature':
                self.options.state(["!disabled"])
            else:
                self.options.state(["disabled"])

            if self.newrow == False:
                if self.varCol <= 4:
                    self.options.grid(column = (self.varCol), row = 1, padx = 8)
                    if self.varCol == 4:
                        self.varCol = 0
                        self.newrow = True
            elif self.newrow == True:
                self.options.grid(column = (self.varCol), row = 2, padx = 8)


    #This is the Temperature menu
    def temperM(self, *args):
        self.clearscreen(self.frame)
        self.frame2 = Frame(self.root)
        self.frame2.grid(column = 0, row = 0)


        self.firstunit = StringVar()
        self.secondunit = StringVar()

        self.entryspace = IntVar()
        self.displayspace = IntVar()

        #Create back button

        #This is the part that needs to be fixed

        self.back = Button(self.frame2, text = "< Back",
         command = lambda: self.redo(self.frame2))
        self.back.grid(column = 1, row = 4)

        self.label = Label(self.frame2, text = "Convert from: ")
        self.label.grid(column = 1, row = 1, padx = 4)

        self.label2 = Label(self.frame2, text = "Convert to: ")
        self.label2.grid(column = 1, row = 2, padx = 4)

        #Create the check boxes

        self.celsius = Checkbutton(self.frame2, text = "Celsius",
         variable = self.firstunit, onvalue = 'celsius')
        self.celsius.grid(column = 2, row = 1, padx = 3)

        self.fahrenheit = Checkbutton(self.frame2, text = "Fahrenheit",
         variable = self.firstunit, onvalue = 'fahrenheit')
        self.fahrenheit.grid(column = 3, row = 1, padx = 3)

        self.kelvin = Checkbutton(self.frame2, text = 'Kelvin',
         variable = self.firstunit, onvalue = 'kelvin')
        self.kelvin.grid(column = 4, row = 1, padx = 3)

        self.celsius2 = Checkbutton(self.frame2, text = "Celsius",
         variable = self.secondunit, onvalue = 'celsius')
        self.celsius2.grid(column = 2, row = 2, padx = 3)

        self.fahrenheit2 = Checkbutton(self.frame2, text = "Fahrenheit",
         variable = self.secondunit, onvalue = 'fahrenheit')
        self.fahrenheit2.grid(column = 3, row = 2, padx = 3)

        self.kelvin2 = Checkbutton(self.frame2, text = 'Kelvin',
         variable = self.secondunit, onvalue = 'kelvin')
        self.kelvin2.grid(column = 4, row = 2, padx = 3)

        #Create entry space to recieve text

        self.entry = Entry(self.frame2, width = 10,
         textvariable = self.entryspace)
        self.entry.grid(column = 4, row = 3)

        self.button = Button(self.frame2, text = "Calculate",
         command = lambda: compute())
        self.button.grid(column = 4, row = 4)

        self.display = Label(self.frame2, textvariable = self.displayspace)
        self.display.grid(column = 3, row = 3)

        self.answer = Label(self.frame2, text = "Answer :")
        self.answer.grid(column = 2, row  = 3)

        self.root.bind('<Return>', lambda e: compute())

        def compute():
            try:
                self.num = self.entryspace.get()
                self.num = round(float(self.num), 3)
                self.calculate = Temperature()

                if self.firstunit.get() == 'celsius' and \
                 self.secondunit.get() == 'fahrenheit':
                    self.displayspace.set(self.calculate.C2F(self.num))

                elif self.firstunit.get() =='celsius' and \
                 self.secondunit.get() == 'kelvin':
                     self.displayspace.set(self.calculate.C2K(self.num))

                elif self.firstunit.get() =='fahrenheit' and \
                 self.secondunit.get() == 'celsius':
                     self.displayspace.set(self.calculate.F2C(self.num))

                elif self.firstunit.get() =='fahrenheit' and \
                 self.secondunit.get() == 'kelvin':
                     self.displayspace.set(self.calculate.F2K(self.num))

                elif self.firstunit.get() =='kelvin' and \
                 self.secondunit.get() == 'celsius':
                     self.displayspace.set(self.calculate.K2C(self.num))

                elif self.firstunit.get() =='kelvin' and \
                 self.secondunit.get() == 'fahrenheit':
                     self.displayspace.set(self.calculate.K2F(self.num))

            except ValueError:
                pass
        return compute()



    def clearscreen(self, window):
        self.window = window
        self.window.destroy()

    def redo(self, window):
        self.window = window
        self.clearscreen(self.window)
        self.mainM()



#This right now is unusable. :(

''''#This class creates the calulation commands for each Unit
 #This is what I'm trying to run
class Calculate(object):
    def __init__(self):
        self.gui = Menus(root)

    def celtoFah(self, *args):
        self.temp = Temperature()
        self.number = float(self.gui.temperM)
        print self.number
        try:
            return self.temp.C2F(self.number)
        except ValueError:
            pass


    def Fahtocel(self):
        self.temp = Temperature
        return self.temp.F2C(self.number)'''



if __name__ == "__main__":
    print ("This is the unit conversion program Alpha v1.1.0.1")
    print ("This program requires that the alpha.py file be in the same " +
    "directory or in the main python library.")
    root = Tk()
    Home = Menus(root)
    root.mainloop()
