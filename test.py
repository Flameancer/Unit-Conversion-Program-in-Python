#Test program to solve problems.

class Foo(object):
    def __init__(self, number):
        self.number = number

    def run(self):
        print "I will now square your number"
        print "Your number squared is: "

#This squares the number
        def calculate():
            return self.number**2

        return calculate()


if __name__ == "__main__":
    test = Foo(input("Choose a number: "))
    print test.run()
