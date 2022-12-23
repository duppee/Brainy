import sys
import hashlib
import sqlite3
import random

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from log import Ui_login
from sub import Ui_Form
from difficult import Ui_Complexity
from test import Ui_Tests
from future import Ui_Future


class MyWidget(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            llog = self.lineEdit.text()
            ppas = self.lineEdit_2.text()

            str = hashlib.sha256(ppas.encode('utf-8'))
            pass_hashed = str.hexdigest()

            # db = sqlite3.connect('Brainy.db')
            #
            # cur = db.cursor()
            #
            #
            #
            # log_bd = cur.execute(f'''SELECT login FROM users WHERE login LIKE "{llog}" ''').fetchone()
            # pass_bd = cur.execute(f'''SELECT pass FROM users WHERE pass LIKE "{ppas}" ''').fetchone()
            #
            # if log_bd and pass_bd:
            #     pass
            # else:
            #     cur.execute(f'''INSERT INTO users(login) VALUES("{llog}")''')
            #     cur.execute(f'''INSERT INTO users(pass) VALUES("{ppas}")''')
            # db.commit()
            # db.close()

            w.hide()
            w2.show()


class MyWidget1(QMainWindow, Ui_Form):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            global d2_ru_eng
            d2_ru_eng = {"Алгебра": "math",
                         "Физика": "physics"}
            self.d2_ru_eng = d2_ru_eng
            self.lst = [
                self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7,
                self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12,
                self.pushButton_13, self.pushButton_14
            ]
            for i in range(len(self.lst)):
                self.lst[i].clicked.connect(self.difficult)

        except Exception as e:
            print(e)

    def difficult(self):
        try:
            if self.sender().objectName() in self.d2_ru_eng:
                self.G = (
                    ''.join([i for i in str(self.sender().geometry())[18:] if i != ',' and i != ')' and i != '('])).split()
                self.W = (''.join(
                    [i for i in str(self.geometry())[18:] if i != ',' and i != ')' and i != '('])).split()
                global w3, w5
                w3 = Difficult(self.G, self.sender().objectName(), self.W)
                w3.show()
            else:
                self.pred = Future()
                self.pred.show()
        except Exception as e:
            print(e)


class Difficult(QMainWindow, Ui_Complexity):
    def __init__(self, G, G1, W):
        super().__init__()
        self.setupUi(self)
        self.label_2.setText(G1)
        self.G1 = G1
        self.G = G
        self.setupUi(self)
        self.setGeometry(int(W[0]) + int(G[0]) - 180, int(W[1]) + int(G[1]) + 30, 182, 164)
        self.lst1 = [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4]
        for i in range(len(self.lst1)):
            self.lst1[i].clicked.connect(self.go)

    def go(self):
        try:
            global vopr
            d1_ru_eng = {"легко": "easy",
                         "нормально": "normal",
                         "сложно": "hard",
                         "олимпиадные задания": "crazy"}



            d1 = str(d1_ru_eng[self.sender().text()])
            d2 = str(d2_ru_eng[self.G1])

            db = sqlite3.connect('Brainy.db')
            cur = db.cursor()

            vopr = cur.execute(f'''SELECT variant.question, variant.answer, variant.mis_one, variant.mis_two, variant.mis_three 
                                FROM variant
                                INNER JOIN subjects ON tests.sub_id = subjects.id
                                INNER JOIN level ON tests.lvl_id = level.id
                                INNER JOIN tests ON variant.test_id = tests.id
                                WHERE level.lvl LIKE "{d1}" AND subjects.name LIKE "{d2}" ''').fetchall()
            if len(vopr) == 0:
                self.w7 = Future()
                self.w7.show()
            else:
                global w5
                w5 = Test(vopr)
                w5.show()
                w2.hide()
                w3.hide()
        except Exception as e:
            print(e)



class Test(QMainWindow, Ui_Tests):
    def __init__(self, vopr):
        self.vopr = vopr
        super().__init__()
        self.setupUi(self)
        self.build()

    def build(self):
        try:
            vopross = [self.vopros1, self.vopros2, self.vopros3, self.vopros4, self.vopros5,
                       self.vopros6, self.vopros7, self.vopros8, self.vopros9, self.vopros10]
            global otv
            for i in range(len(self.vopr)):
                vopross[i].setPlainText(self.vopr[i][0])
            otv = [[self.otv1_1, self.otv1_2, self.otv1_3, self.otv1_4],
                   [self.otv2_1, self.otv2_2, self.otv2_3, self.otv2_4],
                   [self.otv3_1, self.otv3_2, self.otv3_3, self.otv3_4],
                   [self.otv4_1, self.otv4_2, self.otv4_3, self.otv4_4],
                   [self.otv5_1, self.otv5_2, self.otv5_3, self.otv5_4],
                   [self.otv6_1, self.otv6_2, self.otv6_3, self.otv6_4],
                   [self.otv7_1, self.otv7_2, self.otv7_3, self.otv7_4],
                   [self.otv8_1, self.otv8_2, self.otv8_3, self.otv8_4],
                   [self.otv9_1, self.otv9_2, self.otv9_3, self.otv9_4],
                   [self.otv10_1, self.otv10_2, self.otv10_3, self.otv10_4]]
            # lst = []
            # for i in range(0, 40):
            #     lst.append(f'self.otv{i // 4 + 1}_{i % 4 + 1}')
            # print(', '.join(lst))
            for i in range(len(self.vopr)):
                a = [e for e in self.vopr[i][1:]]
                random.shuffle(a)
                for j in range(len(a)):
                    otv[i][j].setText(a[j])

            self.btn.clicked.connect(self.prov)

            # for i in range(len(otv[9])):
            #     otv[9][i].clicked.connect(self.prov)

        except Exception as e:
            print(e)

    def prov(self):
        try:
            ressult = 0
            for i in range(len(otv)):
                for j in range(len(otv[i])):
                    if otv[i][j].isChecked():
                        if otv[i][j].text() == vopr[i][1]:
                            ressult += 1
            self.w6 = Itog(ressult)
            self.w6.show()
        except Exception as e:
            print(e)


class Itog(QMainWindow):
    def __init__(self, ressult):
        self.ressult = ressult
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(700, 500, 280, 100)
        self.setWindowTitle("Итог")

        self.lb1 = QLabel(f"Вы ответили на {str(self.ressult)} верно", self)
        self.lb1.move(24, 18)
        self.lb1.resize(300, 20)
        self.lb1.setFont(QFont("Times", 14))

        self.btn2 = QPushButton(self)
        self.btn2.setText("OK")
        self.btn2.resize(70, 35)
        self.btn2.move(105, 50)
        self.btn2.clicked.connect(self.restrart)

    def restrart(self):
        w2.show()
        self.hide()
        global w5
        w5 = Test(vopr)
        w5.hide()



class Future(QMainWindow, Ui_Future):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.okk)


    def okk(self):
        try:
            self.hide()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    user = [None, None]
    global d2
    d1, d2 = None, None
    app = QApplication(sys.argv)
    w = MyWidget()
    w2 = MyWidget1()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())
