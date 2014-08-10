#Test program to test conversion Library

from alpha import *
def main():
    c = raw_input("What temperature would you like to convert to? ")
    c = str(c)
    print (c)
    if c[0] == "F" or c[0] == "f":
        new_temp = Temperature()
        temp = raw_input("What would you like to convert to? ")
        if temp[0] == "K" or temp[0] == "k":
            temp = input("What is the number you would like to convert? ")
            temp = int(temp)
            print (new_temp.F2K(temp))
main()
