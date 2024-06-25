import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sympy

# pip install PyQt5Designer
# pip install PyQt5
# pip install sympy
# C:\Users\사용자_이름\AppData\Local\Programs\Python\Python39\Lib\site-packages\QtDesigner

form_class = uic.loadUiType("win_app.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.zeroButton.clicked.connect(self.input_number)
        self.oneButton.clicked.connect(self.input_number)
        self.twoButton.clicked.connect(self.input_number)
        self.threeButton.clicked.connect(self.input_number)
        self.fourButton.clicked.connect(self.input_number)
        self.fiveButton.clicked.connect(self.input_number)
        self.sixButton.clicked.connect(self.input_number)
        self.sevenButton.clicked.connect(self.input_number)
        self.eightButton.clicked.connect(self.input_number)
        self.nineButton.clicked.connect(self.input_number)

        self.calcButton.clicked.connect(self.calc)
        self.plusButton.clicked.connect(self.plus)
        self.minusButton.clicked.connect(self.minus)
        self.clearButton.clicked.connect(self.clear)
        self.removeButton.clicked.connect(self.remove)

    def input_number(self):
        display_text = self.display.text()
        object_name = self.sender().objectName()

        if object_name == 'zeroButton':
            display_text += '0'
        elif object_name == 'oneButton':
            display_text += '1'
        elif object_name == 'twoButton':
            display_text += '2'
        elif object_name == 'threeButton':
            display_text += '3'
        elif object_name == 'fourButton':
            display_text += '4'
        elif object_name == 'fiveButton':
            display_text += '5'
        elif object_name == 'sixButton':
            display_text += '6'
        elif object_name == 'sevenButton':
            display_text += '7'
        elif object_name == 'eightButton':
            display_text += '8'
        elif object_name == 'nineButton':
            display_text += '9'

        self.display.setText(display_text)

    def calc(self):
        display_text = self.display.text()
        
        if '=' in display_text:
            return
        
        result = sympy.sympify(display_text)
        display_text += ' = '
        display_text += str(result)

        self.display.setText(display_text)
    
    def plus(self):
        display_text = self.display.text()
        display_text += ' + '
        self.display.setText(display_text)

    def minus(self):
        display_text = self.display.text()
        display_text += ' - '
        self.display.setText(display_text)

    def clear(self):
        self.display.setText('')

    def remove(self):
        display_text = self.display.text()
        self.display.setText(display_text[:-1])

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()