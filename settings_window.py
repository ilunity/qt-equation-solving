from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(530, 170)
        settings_window.setMinimumSize(QtCore.QSize(530, 170))
        settings_window.setMaximumSize(QtCore.QSize(530, 170))
        self.settings_widget = QtWidgets.QTabWidget(settings_window)
        self.settings_widget.setGeometry(QtCore.QRect(0, 0, 530, 170))
        self.settings_widget.setMinimumSize(QtCore.QSize(530, 170))
        self.settings_widget.setMaximumSize(QtCore.QSize(530, 170))
        self.settings_widget.setObjectName("settings_widget")
        self.general_settings_tab = QtWidgets.QWidget()
        self.general_settings_tab.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                                "color: white;\n"
                                                "border-radius: 10px;")
        self.general_settings_tab.setObjectName("general_settings_tab")
        self.accuracy_label = QtWidgets.QLabel(self.general_settings_tab)
        self.accuracy_label.setGeometry(QtCore.QRect(20, 20, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.accuracy_label.setFont(font)
        self.accuracy_label.setObjectName("accuracy_label")
        self.accuracy_after_decimal_point = QtWidgets.QSpinBox(self.general_settings_tab)
        self.accuracy_after_decimal_point.setGeometry(QtCore.QRect(280, 20, 42, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.accuracy_after_decimal_point.setFont(font)
        self.accuracy_after_decimal_point.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                        "border-radius: 3px;\n"
                                                        "color: rgb(41, 105, 255);")
        self.accuracy_after_decimal_point.setObjectName("accuracy_after_decimal_point")
        self.domain_label = QtWidgets.QLabel(self.general_settings_tab)
        self.domain_label.setGeometry(QtCore.QRect(20, 70, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.domain_label.setFont(font)
        self.domain_label.setObjectName("domain_label")
        self.domain_input_label = QtWidgets.QLabel(self.general_settings_tab)
        self.domain_input_label.setGeometry(QtCore.QRect(20, 100, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.domain_input_label.setFont(font)
        self.domain_input_label.setObjectName("domain_input_label")
        self.left_limit_finding_interval = QtWidgets.QLineEdit(self.general_settings_tab)
        self.left_limit_finding_interval.setGeometry(QtCore.QRect(45, 100, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.left_limit_finding_interval.setFont(font)
        self.left_limit_finding_interval.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                       "border-radius: 3px;\n"
                                                       "color: rgb(41, 105, 255);")
        self.left_limit_finding_interval.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.left_limit_finding_interval.setObjectName("left_limit_finding_interval")
        self.right_limit_finding_interval = QtWidgets.QLineEdit(self.general_settings_tab)
        self.right_limit_finding_interval.setGeometry(QtCore.QRect(150, 100, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.right_limit_finding_interval.setFont(font)
        self.right_limit_finding_interval.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                        "border-radius: 3px;\n"
                                                        "color: rgb(41, 105, 255);")
        self.right_limit_finding_interval.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.right_limit_finding_interval.setObjectName("right_limit_finding_interval")
        self.save_general_settings_btn = QtWidgets.QPushButton(self.general_settings_tab)
        self.save_general_settings_btn.setGeometry(QtCore.QRect(410, 100, 90, 30))
        self.save_general_settings_btn.setStyleSheet("#save_general_settings_btn {\n"
                                                     "    background-color: rgb(0, 129, 194);\n"
                                                     "    color: white;\n"
                                                     "    border-radius: 5px;\n"
                                                     "}\n"
                                                     "#save_general_settings_btn:hover {\n"
                                                     "    background-color: rgb(2, 190, 218);\n"
                                                     "} \n"
                                                     "#save_general_settings_btn:pressed {\n"
                                                     "    background-color: rgb(23, 92, 252);\n"
                                                     "}")
        self.save_general_settings_btn.setObjectName("save_general_settings_btn")
        self.settings_widget.addTab(self.general_settings_tab, "")
        self.research_settings_tab = QtWidgets.QWidget()
        self.research_settings_tab.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                                 "color: white;\n"
                                                 "border-radius: 10px;")
        self.research_settings_tab.setObjectName("research_settings_tab")
        self.comparing_label = QtWidgets.QLabel(self.research_settings_tab)
        self.comparing_label.setGeometry(QtCore.QRect(20, 20, 451, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comparing_label.setFont(font)
        self.comparing_label.setObjectName("comparing_label")
        self.first_convergence_label = QtWidgets.QLabel(self.research_settings_tab)
        self.first_convergence_label.setGeometry(QtCore.QRect(20, 50, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.first_convergence_label.setFont(font)
        self.first_convergence_label.setObjectName("first_convergence_label")
        self.second_convergence_label = QtWidgets.QLabel(self.research_settings_tab)
        self.second_convergence_label.setGeometry(QtCore.QRect(20, 80, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.second_convergence_label.setFont(font)
        self.second_convergence_label.setObjectName("second_convergence_label")
        self.third_convergence_label = QtWidgets.QLabel(self.research_settings_tab)
        self.third_convergence_label.setGeometry(QtCore.QRect(20, 110, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.third_convergence_label.setFont(font)
        self.third_convergence_label.setObjectName("third_convergence_label")
        self.first_convergence_value = QtWidgets.QSpinBox(self.research_settings_tab)
        self.first_convergence_value.setGeometry(QtCore.QRect(170, 50, 42, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.first_convergence_value.setFont(font)
        self.first_convergence_value.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                   "border-radius: 3px;\n"
                                                   "color: rgb(41, 105, 255);")
        self.first_convergence_value.setObjectName("first_convergence_value")
        self.second_convergence_value = QtWidgets.QSpinBox(self.research_settings_tab)
        self.second_convergence_value.setGeometry(QtCore.QRect(170, 80, 42, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.second_convergence_value.setFont(font)
        self.second_convergence_value.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                    "border-radius: 3px;\n"
                                                    "color: rgb(41, 105, 255);")
        self.second_convergence_value.setObjectName("second_convergence_value")
        self.third_convergence_value = QtWidgets.QSpinBox(self.research_settings_tab)
        self.third_convergence_value.setGeometry(QtCore.QRect(170, 110, 42, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.third_convergence_value.setFont(font)
        self.third_convergence_value.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                                   "border-radius: 3px;\n"
                                                   "color: rgb(41, 105, 255);")
        self.third_convergence_value.setObjectName("third_convergence_value")
        self.save_research_settings_btn = QtWidgets.QPushButton(self.research_settings_tab)
        self.save_research_settings_btn.setGeometry(QtCore.QRect(410, 100, 90, 30))
        self.save_research_settings_btn.setStyleSheet("#save_research_settings_btn {\n"
                                                      "    background-color: rgb(0, 129, 194);\n"
                                                      "    color: white;\n"
                                                      "    border-radius: 5px;\n"
                                                      "}\n"
                                                      "#save_research_settings_btn:hover {\n"
                                                      "    background-color: rgb(2, 190, 218);\n"
                                                      "} \n"
                                                      "#save_research_settings_btn:pressed {\n"
                                                      "    background-color: rgb(23, 92, 252);\n"
                                                      "}")
        self.save_research_settings_btn.setObjectName("save_research_settings_btn")
        self.settings_widget.addTab(self.research_settings_tab, "")

        self.retranslateUi(settings_window)
        self.settings_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(settings_window)

        self.load_data()
        self.event_handler()

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "Настройки"))
        self.accuracy_label.setText(
            _translate("settings_window", "Точность вычисления корня. До             знака после запятой."))
        self.domain_label.setText(_translate("settings_window", "Область поиска интервалов, содержащих корень:"))
        self.domain_input_label.setText(_translate("settings_window", "От               до"))
        self.save_general_settings_btn.setText(_translate("settings_window", "Сохранить"))
        self.settings_widget.setTabText(self.settings_widget.indexOf(self.general_settings_tab),
                                        _translate("settings_window", "Общие"))
        self.comparing_label.setText(
            _translate("settings_window", "Сравнение скорости сходимости от заданной точности:"))
        self.first_convergence_label.setText(_translate("settings_window", "Первое значение: "))
        self.second_convergence_label.setText(_translate("settings_window", "Второе значение: "))
        self.save_research_settings_btn.setText(_translate("settings_window", "Сохранить"))
        self.third_convergence_label.setText(_translate("settings_window", "Третье значение:"))
        self.settings_widget.setTabText(self.settings_widget.indexOf(self.research_settings_tab),
                                        _translate("settings_window", "Параметры исследования"))

    def load_data(self):
        with open("data/settings_data.json", "r") as file:
            self.settings_data = json.load(file)
        self.accuracy_after_decimal_point.setSpecialValueText(str(self.settings_data["general"]["accuracy"]))
        self.left_limit_finding_interval.setText(str(self.settings_data["general"]["left_interval"]))
        self.right_limit_finding_interval.setText(str(self.settings_data["general"]["right_interval"]))

        self.first_convergence_value.setSpecialValueText(
            str(self.settings_data["comparing"]["first_accuracy"]))
        self.second_convergence_value.setSpecialValueText(
            str(self.settings_data["comparing"]["second_accuracy"]))
        self.third_convergence_value.setSpecialValueText(
            str(self.settings_data["comparing"]["third_accuracy"]))

    def event_handler(self):
        self.save_general_settings_btn.clicked.connect(self.save_settings)
        self.save_research_settings_btn.clicked.connect(self.save_settings)

    def save_settings(self):
        # todo Проверять на ошибки типа
        self.settings_data["general"]["accuracy"] = int(self.accuracy_after_decimal_point.text())
        self.settings_data["general"]["left_interval"] = int(self.left_limit_finding_interval.text())
        self.settings_data["general"]["right_interval"] = int(self.right_limit_finding_interval.text())

        self.settings_data["comparing"]["first_accuracy"] = int(self.first_convergence_value.text())
        self.settings_data["comparing"]["second_accuracy"] = int(self.second_convergence_value.text())
        self.settings_data["comparing"]["third_accuracy"] = int(self.third_convergence_value.text())

        with open("data/settings_data.json", "w") as file:
            json.dump(self.settings_data, file, indent=3, ensure_ascii=False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    settings_window = Ui_settings_window()
    settings_window.setupUi(Window)
    Window.show()

    sys.exit(app.exec_())
