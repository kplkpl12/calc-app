class App():
    def __init__(self):
        self.number = 0

    def plus(self, value):
        self.number += value

    def minus(self, value):
        self.number -= value

    def print_result(self):
        print(self.number)


if __name__ == "__main__" :
    app = App()
    app.plus(5)
    app.minus(-10)
    app.plus(2)
    app.minus(-3)
    app.print_result()