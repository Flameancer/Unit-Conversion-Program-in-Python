#Jonathan Harris
#August 5, 2014
#Conversion Library
#Build #: Alpha 1.0.0.0

""" This is the basis unit conversion library made in python for my unit
conversion program. The basis behind this is to get used to making programs in
python as well as making GUI."""

#Temperature Class
class Temperature:

    """The Conversion from Celsius to Fahrenheit"""
    def C2F(self,Celsius):
        self.Celsius = Celsius
        self.Fahrenheit = (self.Celsius*9)/5 + 32
        return self.Fahrenheit

    """The Conversion from Fahrenheit to Celsius"""
    def F2C(self, Fahrenheit):
        self.Fahrenheit = Fahrenheit
        self.Celsius = ((self.Fahrenheit-32)*5)/9
        return self.Celsius

    """The Conversion from Kelvin to Celsius"""
    def K2C(self, Kelvin):
        self.Kelvin = Kelvin
        self.Celsius = self.Kelvin - 273.15
        return self.Celsius

    """The Conversion from Celsius to Kelvin"""
    def C2K(self, Celsius):
        self.Celsius = Celsius
        self.Kelvin = self.Celsius + 273.15
        return self.Kelvin

    """The Conversion from Kelvin to Fahrenheit"""
    def K2F(self, Kelvin):
        self.Kelvin = Kelvin
        self.Fahrenheit = 1.8*(Self.Kelvin)+32
        return self.Fahrenheit

    """The Conversion from Fahrenheit to Kelvin"""
    def F2K(self, Fahrenheit):
        self.Fahrenheit = Fahrenheit
        self.Celsius = ((self.Fahrenheit-32)*5)/9
        self.Kelvin = self.Celsius + 273.15
        return self.Kelvin
