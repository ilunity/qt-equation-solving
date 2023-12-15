import json
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_input_intervals(object):
    def setupUi(self, input_intervals):
        input_intervals.setObjectName("input_intervals")
        input_intervals.resize(566, 236)
        input_intervals.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                      "color: white;")

        self.entered_intervals_text = QtWidgets.QLabel(input_intervals)
        self.entered_intervals_text.setGeometry(QtCore.QRect(410, 20, 130, 190))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.entered_intervals_text.setFont(font)
        self.entered_intervals_text.setStyleSheet("background-color: rgb(121, 121, 121);\n"
                                                  "border-radius: 5px;\n"
                                                  "padding-top: 2px;")
        self.entered_intervals_text.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.entered_intervals_text.setObjectName("entered_intervals_text")

        self.input_interval_frame = QtWidgets.QFrame(input_intervals)
        self.input_interval_frame.setGeometry(QtCore.QRect(20, 20, 351, 191))
        self.input_interval_frame.setStyleSheet("background-color: rgb(121, 121, 121);\n"
                                                "border-radius: 5px;")
        self.input_interval_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_interval_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_interval_frame.setObjectName("input_interval_frame")
        self.input_interval_label = QtWidgets.QLabel(self.input_interval_frame)
        self.input_interval_label.setGeometry(QtCore.QRect(10, 10, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_interval_label.setFont(font)
        self.input_interval_label.setObjectName("input_interval_label")
        self.left_limit_of_interval = QtWidgets.QLineEdit(self.input_interval_frame)
        self.left_limit_of_interval.setGeometry(QtCore.QRect(40, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.left_limit_of_interval.setFont(font)
        self.left_limit_of_interval.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                  "border-radius: 3px;\n"
                                                  "color: rgb(41, 105, 255);")
        self.left_limit_of_interval.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.left_limit_of_interval.setObjectName("left_limit_of_interval")
        self.right_limit_of_interval = QtWidgets.QLineEdit(self.input_interval_frame)
        self.right_limit_of_interval.setGeometry(QtCore.QRect(140, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.right_limit_of_interval.setFont(font)
        self.right_limit_of_interval.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                   "border-radius: 3px;\n"
                                                   "color: rgb(41, 105, 255);")
        self.right_limit_of_interval.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.right_limit_of_interval.setObjectName("right_limit_of_interval")
        self.add_interval_btn = QtWidgets.QPushButton(self.input_interval_frame)
        self.add_interval_btn.setGeometry(QtCore.QRect(10, 150, 90, 30))
        self.add_interval_btn.setStyleSheet("#add_interval_btn {\n"
                                            "    background-color: rgb(0, 129, 194);\n"
                                            "    color: white;\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "#add_interval_btn:hover {\n"
                                            "    background-color: rgb(2, 190, 218);\n"
                                            "} \n"
                                            "#add_interval_btn:pressed {\n"
                                            "    background-color: rgb(23, 92, 252);\n"
                                            "}")
        self.add_interval_btn.setObjectName("add_interval_btn")
        self.delete_interval_btn = QtWidgets.QPushButton(self.input_interval_frame)
        self.delete_interval_btn.setGeometry(QtCore.QRect(150, 150, 90, 30))
        self.delete_interval_btn.setStyleSheet("#delete_interval_btn {\n"
                                               "    background-color: rgb(191, 4, 10);\n"
                                               "    color: white;\n"
                                               "    border-radius: 5px;\n"
                                               "}\n"
                                               "#delete_interval_btn:hover {\n"
                                               "    background-color: rgb(255, 0, 4);\n"
                                               "} \n"
                                               "#delete_interval_btn:pressed {\n"
                                               "    background-color: rgb(180, 0, 3);\n"
                                               "}")
        self.delete_interval_btn.setObjectName("delete_interval_btn")
        self.reset_interval_btn = QtWidgets.QPushButton(self.input_interval_frame)
        self.reset_interval_btn.setGeometry(QtCore.QRect(250, 150, 90, 30))
        self.reset_interval_btn.setStyleSheet("#reset_interval_btn {\n"
                                              "    background-color: rgb(57, 156, 39);\n"
                                              "    color: white;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              "#reset_interval_btn:hover {\n"
                                              "    background-color: rgb(113, 180, 67);\n"
                                              "} \n"
                                              "#reset_interval_btn:pressed {\n"
                                              "    background-color: rgb(84, 132, 49);\n"
                                              "}")
        self.reset_interval_btn.setObjectName("reset_interval_btn")
        self.domain_input_label = QtWidgets.QLabel(self.input_interval_frame)
        self.domain_input_label.setGeometry(QtCore.QRect(10, 60, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.domain_input_label.setFont(font)
        self.domain_input_label.setObjectName("domain_input_label")
        self.reset_interval_btn.raise_()
        self.input_interval_label.raise_()
        self.right_limit_of_interval.raise_()
        self.delete_interval_btn.raise_()
        self.add_interval_btn.raise_()
        self.domain_input_label.raise_()
        self.left_limit_of_interval.raise_()

        self.retranslateUi(input_intervals)
        QtCore.QMetaObject.connectSlotsByName(input_intervals)

        self.load_data()
        self.event_handler()

    def retranslateUi(self, input_intervals):
        _translate = QtCore.QCoreApplication.translate
        input_intervals.setWindowTitle(_translate("input_intervals", "Ввод интервалов"))
        self.reset_interval_btn.setText(_translate("input_intervals", "Сбросить"))
        self.input_interval_label.setText(_translate("input_intervals", "Задайте левый и правый конец интервала:"))
        self.delete_interval_btn.setText(_translate("input_intervals", "Удалить"))
        self.add_interval_btn.setText(_translate("input_intervals", "Добавить"))
        self.domain_input_label.setText(_translate("input_intervals", "От               до"))

    def refresh_entered_intervals_text(self):
        output_message = ""
        for interval in self.intervals_data["intervals"]:
            output_message += f'[{interval[0]}, {interval[1]}]\n'

        self.entered_intervals_text.setText(output_message)

    def load_data(self):
        with open("data/intervals_data.json", "r") as file:
            self.intervals_data = json.load(file)

        if len(self.intervals_data) == 0:
            return

        self.refresh_entered_intervals_text()

    def event_handler(self):
        self.add_interval_btn.clicked.connect(self.add_interval)
        self.delete_interval_btn.clicked.connect(self.delete_last_interval)
        self.reset_interval_btn.clicked.connect(self.reset_intervals)

    def add_interval(self):

        def input_interval():
            input_text_array = [self.left_limit_of_interval.text(), self.right_limit_of_interval.text()]
            interval = [float(x) for x in filter(lambda inp_txt: inp_txt != "", input_text_array)]
            return interval

        def update_intervals_data(interval):
            self.intervals_data["intervals"].append(interval)

            with open("data/intervals_data.json", "w") as file:
                json.dump(self.intervals_data, file, indent=3, ensure_ascii=False)

        def update_entered_intervals_text(interval):
            current_intervals = self.entered_intervals_text.text()
            next_interval = f'[{interval[0]}, {interval[1]}]\n'
            self.entered_intervals_text.setText(f'{current_intervals}{next_interval}')

        def reset_limit_text():
            self.left_limit_of_interval.setText("")
            self.right_limit_of_interval.setText("")

        new_interval = input_interval()

        if len(new_interval) != 2:
            return

        update_intervals_data(new_interval)
        update_entered_intervals_text(new_interval)
        reset_limit_text()

    def delete_last_interval(self):
        if len(self.intervals_data["intervals"]) == 0:
            return
        self.intervals_data["intervals"].pop()
        with open("data/intervals_data.json", "w") as file:
            json.dump(self.intervals_data, file, indent=3, ensure_ascii=False)

        self.refresh_entered_intervals_text()

    def reset_intervals(self):
        self.intervals_data = {"intervals": []}
        with open("data/intervals_data.json", "w") as file:
            json.dump(self.intervals_data, file, indent=3, ensure_ascii=False)
        self.entered_intervals_text.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    input_window = Ui_input_intervals()
    input_window.setupUi(Window)
    Window.show()

    sys.exit(app.exec_())
