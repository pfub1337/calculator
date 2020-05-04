import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
# from EasyMode_ui import Ui_EzMainWindow
# from AdvancedMode_ui import Ui_AdvMainWindow


class EasyMode(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('EasyMode.ui', self)
        # self.setupUi(self)

        # Display text
        self.text = self.display.text()

        # Lists
        self.numbers = ['']
        self.operations = list()

        # Numbers buttons
        self.oneBtn.clicked.connect(self.One)
        self.twoBtn.clicked.connect(self.Two)
        self.threeBtn.clicked.connect(self.Three)
        self.fourBtn.clicked.connect(self.Four)
        self.fiveBtn.clicked.connect(self.Five)
        self.sixBtn.clicked.connect(self.Six)
        self.sevenBtn.clicked.connect(self.Seven)
        self.eightBtn.clicked.connect(self.Eight)
        self.nineBtn.clicked.connect(self.Nine)
        self.zeroBtn.clicked.connect(self.Zero)
        self.dotBtn.clicked.connect(self.Dot)
        # Operations buttons
        self.clearBtn.clicked.connect(self.Clear)
        self.backspaceBtn.clicked.connect(self.Backspace)
        self.plusBtn.clicked.connect(self.Plus)
        self.minusBtn.clicked.connect(self.Minus)
        self.totalBtn.clicked.connect(self.Total)
        self.multiplyBtn.clicked.connect(self.Multiply)
        self.divBtn.clicked.connect(self.Div)
        self.advancedMode.triggered.connect(self.AdvancedModeShow)


    def One(self):
        self.text = self.display.text()
        self.display.setText(self.text + '1')
        self.numbers[-1] += '1'

    def Two(self):
        self.text = self.display.text()
        self.display.setText(self.text + '2')
        self.numbers[-1] += '2'

    def Three(self):
        self.text = self.display.text()
        self.display.setText(self.text + '3')
        self.numbers[-1] += '3'

    def Four(self):
        self.text = self.display.text()
        self.display.setText(self.text + '4')
        self.numbers[-1] += '4'

    def Five(self):
        self.text = self.display.text()
        self.display.setText(self.text + '5')
        self.numbers[-1] += '5'

    def Six(self):
        self.text = self.display.text()
        self.display.setText(self.text + '6')
        self.numbers[-1] += '6'

    def Seven(self):
        self.text = self.display.text()
        self.display.setText(self.text + '7')
        self.numbers[-1] += '7'

    def Eight(self):
        self.text = self.display.text()
        self.display.setText(self.text + '8')
        self.numbers[-1] += '8'

    def Nine(self):
        self.text = self.display.text()
        self.display.setText(self.text + '9')
        self.numbers[-1] += '9'

    def Zero(self):
        self.text = self.display.text()
        if self.numbers[-1] == '0':
            return
        else:
            self.display.setText(self.text + '0')
            self.numbers[-1] += '0'

    def Dot(self):
        self.text = self.display.text()
        if '.' in self.numbers[-1]:
            return
        elif self.numbers[-1] == '':
            self.display.setText(self.text + '0.')
            self.numbers[-1] += '0.'
        else:
            self.display.setText(self.text + '.')
            self.numbers[-1] += '.'

    def Clear(self):
        self.displaySec.setText(self.text)
        self.display.setText('')
        self.numbers = ['']
        self.operations = []

    def Backspace(self):
        self.text = self.display.text()
        if self.text == '':
            return
        elif self.text[-1] in '+-*/':
            self.display.setText(self.text[:len(self.text) - 1])
            self.text = self.display.text()
            self.numbers.pop()
            self.operations.pop()
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text[:len(self.text) - 1])
            self.text = self.display.text()
            number = self.numbers[-1]
            self.numbers[-1] = number[:len(number) - 1]

    def Plus(self):
        self.text = self.display.text()
        if (self.text == '') or (self.text[-1] == '+'):
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '+')
            self.numbers.append('')
            self.operations.append('+')

        elif self.text[-1] in '*/-^':
            self.Backspace()
            self.display.setText(self.text + '+')


    def Minus(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] == '-':
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '-')
            self.numbers.append('')
            self.operations.append('-')
        elif self.text[-1] in '*/+^':
            self.Backspace()
            self.display.setText(self.text + '-')

    def Multiply(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] == '*':
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '*')
            self.numbers.append('')
            self.operations.append('*')
        elif self.text[-1] in '-/+^':
            self.Backspace()
            self.display.setText(self.text + '*')

    def Div(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] == '/':
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '/')
            self.numbers.append('')
            self.operations.append('/')
        elif self.text[-1] in '*-+^':
            self.Backspace()
            self.display.setText(self.text + '/')


    def Total(self):
        self.text = self.display.text()
        if self.text == '' or self.operations == [] or len(self.operations) == len(self.numbers):
            return
        elif '*' in self.operations:
            index = self.operations.index('*')
            total = float(self.numbers[index]) * float(self.numbers[index + 1])
            self.numbers[index] = str(total)
            self.numbers.pop(index + 1)
            self.operations.pop(index)
        elif '/' in self.operations:
            index = self.operations.index('/')
            if self.numbers[index + 1] == '0':
                self.display.setText('ERROR')
                return
            else:
                total = float(self.numbers[index]) / float(self.numbers[index + 1])
                self.numbers[index] = str(total)
                self.numbers.pop(index + 1)
                self.operations.pop(index)
        else:
            for i in range(len(self.operations)):
                if self.operations[0] == '+':
                    total = float(self.numbers[0]) + float(self.numbers[1])
                    self.numbers[0] = str(total)
                    self.numbers.pop(1)
                    self.operations.pop(0)
                elif self.operations[0] == '-':
                    total = float(self.numbers[0]) - float(self.numbers[1])
                    self.numbers[0] = str(total)
                    self.numbers.pop(1)
                    self.operations.pop(0)
        self.displaySec.setText(self.text)
        self.display.setText(str(total))

    # Функция переключения между режимами не работает
    def AdvancedModeShow(self):
        AdvMode.show()
        EzMode.close()


class AdvancedMode(EasyMode):
    def __init__(self):
        super().__init__()
        uic.loadUi('AdvancedMode.ui', self)
        # self.setupUi(self)

        # Lists
        self.numbers = ['']
        self.operations = list()

        # Numbers buttons
        self.oneBtn.clicked.connect(self.One)
        self.twoBtn.clicked.connect(self.Two)
        self.threeBtn.clicked.connect(self.Three)
        self.fourBtn.clicked.connect(self.Four)
        self.fiveBtn.clicked.connect(self.Five)
        self.sixBtn.clicked.connect(self.Six)
        self.sevenBtn.clicked.connect(self.Seven)
        self.eightBtn.clicked.connect(self.Eight)
        self.nineBtn.clicked.connect(self.Nine)
        self.zeroBtn.clicked.connect(self.Zero)
        self.dotBtn.clicked.connect(self.Dot)
        # Operations buttons
        self.clearBtn.clicked.connect(self.Clear)
        self.backspaceBtn.clicked.connect(self.Backspace)
        self.plusBtn.clicked.connect(self.Plus)
        self.minusBtn.clicked.connect(self.Minus)
        self.totalBtn.clicked.connect(self.Total)
        self.multiplyBtn.clicked.connect(self.Multiply)
        self.divBtn.clicked.connect(self.Div)
        self.sqrBtn.clicked.connect(self.Square)
        self.piBtn.clicked.connect(self.Pi)
        self.easyMode.triggered.connect(self.EasyModeShow)
        self.exponentBtn.clicked.connect(self.Exponent)
        self.eBtn.clicked.connect(self.E)

    def Pi(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] in '-/+^*':
            self.numbers[-1] = str(math.pi)
            self.display.setText(self.text + 'π')
        elif self.text[-1] == 'π':
            return
        elif self.text[-1] in '1234567890e':
            self.display.setText(self.text + '*π')
            self.operations.append('*')
            self.numbers.append(str(math.pi))

    def E(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] in '-/+^*':
            self.numbers[-1] = str(math.e)
            self.display.setText(self.text + 'e')
        elif self.text[-1] == 'e':
            return
        elif self.text[-1] in '1234567890π':
            self.display.setText(self.text + '*e')
            self.operations.append('*')
            self.numbers.append(str(math.e))

    def Square(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] == '^':
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '^2')
            self.numbers.append('2')
            self.operations.append('^')
        elif self.text[-1] in '-/+':
            self.Backspace()
            self.display.setText(self.text + '^2')
            self.numbers.append('2')
            self.operations.append('^')

    def Exponent(self):
        self.text = self.display.text()
        if self.text == '' or self.text[-1] == '^':
            return
        elif self.text[-1] in '1234567890πe':
            self.display.setText(self.text + '^')
            self.numbers.append('')
            self.operations.append('^')
        elif self.text[-1] in '-/+':
            self.Backspace()
            self.display.setText(self.text + '^')
            self.numbers.append('')
            self.operations.append('^')


    def Total(self):
        self.text = self.display.text()
        if self.text == '' or self.operations == [] or len(self.operations) == len(self.numbers):
            return
        if '^' in self.operations:
                index = self.operations.index('^')
                total = float(self.numbers[index]) ** float(self.numbers[index + 1])
                self.numbers[index] = str(total)
                self.numbers.pop(index + 1)
                self.operations.pop(index)
        elif '*' in self.operations:
                index = self.operations.index('*')
                total = float(self.numbers[index]) * float(self.numbers[index + 1])
                self.numbers[index] = str(total)
                self.numbers.pop(index + 1)
                self.operations.pop(index)
        elif '/' in self.operations:
                index = self.operations.index('/')
                if self.numbers[index + 1] == '0':
                    self.display.setText('ERROR')
                    self.displaySec.setText(self.text)
                    return
                else:
                    total = float(self.numbers[index]) / float(self.numbers[index + 1])
                    self.numbers[index] = str(total)
                    self.numbers.pop(index + 1)
                    self.operations.pop(index)

        for i in range(len(self.operations)):
            if self.operations[0] == '+':
                total = float(self.numbers[0]) + float(self.numbers[1])
                self.numbers[0] = str(total)
                self.numbers.pop(1)
                self.operations.pop(0)
            elif self.operations[0] == '-':
                total = float(self.numbers[0]) - float(self.numbers[1])
                self.numbers[0] = str(total)
                self.numbers.pop(1)
                self.operations.pop(0)
        self.displaySec.setText(self.text)
        self.display.setText(str(total))

    def EasyModeShow(self):
        EzMode.show()
        AdvMode.close()


app = QApplication(sys.argv)
EzMode = EasyMode()
AdvMode = AdvancedMode()
EzMode.show()
sys.exit(app.exec_())