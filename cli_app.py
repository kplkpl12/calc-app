import sys

class cliApp():
    def __init__(self) :
        argv = sys.argv
        self.number = 0
        self.operator = argv[1]
        self.number1 = int (argv[2])
        self.number2 = int (argv[3])

    def plus(self, value):
        self.number += value

    def minus(self, value):
        self.number -= value

    def print_result(self):
        print(self.number)


if __name__ == "__main__" :
    app = cliApp()

    operator = app.operator
    number1 = app.number1
    number2 = app.number2

    if operator == '+':
        app.plus(number1)
        app.plus(number2)
    elif operator == '-':
        app.plus(number1)
        app.minus(number2)

    app.print_result()