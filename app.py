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
    app.plus(9)
    app.minus(13)
    app.plus(-4)
    app.minus(1)
    app.print_result()