class App():
    def __init__(self):
        self.number = 0

    def plus(self, value):
        self.number += value

    def minus(self, value):
        self.number -= value

    def divide(self, value) :
        self.number /= value

    def multiplie(self, value) :
        self.number *= value

    def print_result(self):
        print(self.number)


if __name__ == "__main__" :
    app = App()
    app.plus(9)
    app.multiplie(2)
    app.divide(5)
    app.print_result()