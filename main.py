from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pyqtgraph import PlotWidget
import pyqtgraph

import json

import solving as slv
import settings_window as sw
import input_intervals_window as iw
import research_result as rr


class Ui_MainWindow(object):
    NO_ROOTS_WARNING = "No roots"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 660)
        MainWindow.setMinimumSize(QtCore.QSize(1240, 660))
        MainWindow.setMaximumSize(QtCore.QSize(1240, 660))
        MainWindow.setStyleSheet("")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("#central_widget {\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(64, 255, 118, 255), stop:0.452736 rgba(65, 146, 188, 255), stop:1 rgba(67, 43, 255, 255));\n"
                                          "}")
        self.central_widget.setObjectName("central_widget")
        self.settings_btn = QtWidgets.QPushButton(self.central_widget)
        self.settings_btn.setGeometry(QtCore.QRect(20, 0, 80, 30))
        self.settings_btn.setStyleSheet("#settings_btn {\n"
                                        "    background-color: rgb(134, 134, 134);\n"
                                        "    color: white;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "#settings_btn:hover {\n"
                                        "    background-color: rgb(104, 104, 104);\n"
                                        "} \n"
                                        "#settings_btn:pressed {\n"
                                        "    background-color: rgb(173, 173, 173);\n"
                                        "}")
        self.settings_btn.setObjectName("settings_btn")
        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1200, 610))
        self.frame.setMinimumSize(QtCore.QSize(1200, 610))
        self.frame.setMaximumSize(QtCore.QSize(1200, 610))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1524, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.container = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.container.setContentsMargins(0, 0, 0, 0)
        self.container.setObjectName("container")
        self.info_frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.info_frame.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.info_frame.setFont(font)
        self.info_frame.setStyleSheet("#info_frame {\n"
                                      "    background-color: rgba(107, 112, 111, 35%);\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.info_label = QtWidgets.QLabel(self.info_frame)
        self.info_label.setGeometry(QtCore.QRect(10, 0, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(24)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.solve_btn = QtWidgets.QPushButton(self.info_frame)
        self.solve_btn.setGeometry(QtCore.QRect(110, 290, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.solve_btn.setFont(font)
        self.solve_btn.setStyleSheet("#solve_btn {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "    color: white;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "#solve_btn:hover {\n"
                                     "    background-color: rgb(76, 133, 255);\n"
                                     "} \n"
                                     "#solve_btn:pressed {\n"
                                     "    background-color: rgb(99, 201, 255);\n"
                                     "}")
        self.solve_btn.setObjectName("solve_btn")
        self.input_equation = QtWidgets.QLineEdit(self.info_frame)
        self.input_equation.setGeometry(QtCore.QRect(50, 60, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Mathcad UniMath")
        font.setPointSize(11)
        font.setItalic(True)
        self.input_equation.setFont(font)
        self.input_equation.setObjectName("input_equation")
        self.compare_method_ckbx = QtWidgets.QCheckBox(self.info_frame)
        self.compare_method_ckbx.setGeometry(QtCore.QRect(40, 110, 340, 20))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        self.compare_method_ckbx.setFont(font)
        self.compare_method_ckbx.setObjectName("compare_method_ckbx")
        self.input_intervals_label = QtWidgets.QLabel(self.info_frame)
        self.input_intervals_label.setGeometry(QtCore.QRect(65, 160, 320, 20))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        self.input_intervals_label.setFont(font)
        self.input_intervals_label.setObjectName("input_intervals_label")
        self.input_intervals_btn = QtWidgets.QToolButton(self.info_frame)
        self.input_intervals_btn.setGeometry(QtCore.QRect(40, 160, 20, 20))
        self.input_intervals_btn.setObjectName("input_intervals_btn")
        self.input_intervals_info_label = QtWidgets.QLabel(self.info_frame)
        self.input_intervals_info_label.setEnabled(True)
        self.input_intervals_info_label.setGeometry(QtCore.QRect(65, 190, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_intervals_info_label.setFont(font)
        self.input_intervals_info_label.setStyleSheet("color: rgb(54, 54, 54);\n"
                                                      "padding: 0px;\n"
                                                      "line-height: 0;")
        self.input_intervals_info_label.setWordWrap(True)
        self.input_intervals_info_label.setObjectName("input_intervals_info_label")
        self.result_label = QtWidgets.QLabel(self.info_frame)
        self.result_label.setGeometry(QtCore.QRect(20, 400, 360, 190))
        self.result_label.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                        "border-radius: 5px;")
        self.result_label.setText("")
        self.result_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.result_label.setObjectName("result_label")
        self.container.addWidget(self.info_frame)
        self.graph_view = PlotWidget(self.horizontalLayoutWidget)
        self.graph_view.setMinimumSize(QtCore.QSize(800, 0))
        self.graph_view.setStyleSheet("#graph_view {\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.graph_view.setObjectName("graph_view")
        self.container.addWidget(self.graph_view)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.event_handler()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settings_btn.setText(_translate("MainWindow", "Настройки"))
        self.info_label.setText(_translate("MainWindow", "Введите уравнение от x:"))
        self.solve_btn.setText(_translate("MainWindow", "Решить уравнение"))
        self.compare_method_ckbx.setText(_translate("MainWindow", "Исследовать скорость сходимости"))
        self.input_intervals_label.setText(_translate("MainWindow", "Ввести свои интервалы для поиска"))
        self.input_intervals_btn.setText(_translate("MainWindow", "..."))
        self.input_intervals_info_label.setText(_translate("MainWindow",
                                                           "<html><head/><body><p>Если интервалы не заданы вручную, то они будут найдены автоматически </p></body></html>"))

    def event_handler(self):
        self.solve_btn.clicked.connect(self.btn_solve_handler)
        self.settings_btn.clicked.connect(self.exec_settings)
        self.input_intervals_btn.clicked.connect(self.exec_input_intervals)

    def exec_settings(self):
        self.settings = QtWidgets.QMainWindow()
        self.settings_ui = sw.Ui_settings_window()
        self.settings_ui.setupUi(self.settings)
        self.settings.show()

    def exec_input_intervals(self):
        self.input_intervals = QtWidgets.QMainWindow()
        self.input_intervals_ui = iw.Ui_input_intervals()
        self.input_intervals_ui.setupUi(self.input_intervals)
        self.input_intervals.show()

    def btn_solve_handler(self):
        self.clear_graph()
        self.finding_roots()

    def show_warning_message(self, warning_type):
        def create_warning_window():
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset)
            return error

        def define_warning_message(warning_type):
            if warning_type == self.NO_ROOTS_WARNING:
                return "Да данном промежутке корней нет."
            # if warning_type == self.NO_CHANGE_WARNING:
            #     return "Выражение не было изменено."

        def btn_handler(btn):
            if btn.text() == "Reset":
                self.input_equation.setText("")

        warning_window = create_warning_window()
        warning_window.setText(define_warning_message(warning_type))
        warning_window.buttonClicked.connect(btn_handler)

        warning_window.exec_()

    def save_research_result(self, comparing_accuracy, chord_results, binary_results):
        accuracy_set = []
        for value in comparing_accuracy.values():
            accuracy_set.append(value)

        research_data = {
            "compared_accuracy": accuracy_set,
            "iteration_number": {
                "chord_method": chord_results,
                "binary_method": binary_results
            }
        }
        with open("data/research_data.json", "w") as file:
            json.dump(research_data, file, indent=3, ensure_ascii=False)

    def output_result(self, func, roots, accuracy):
        if len(roots) == 0:
            self.result_label.setText("\n Корни на данных интервалах не найдены.")
        else:
            self.print_roots(roots, accuracy)
            only_number_roots_arr = [x for x in roots if (x != "null" and x != "iter_error")]

            if len(only_number_roots_arr) > 0:
                self.show_graph(func, only_number_roots_arr)
            else:
                self.show_warning_message(self.NO_ROOTS_WARNING)

    def show_research_result(self):
        self.research_result = QtWidgets.QMainWindow()
        self.research_result_ui = rr.Ui_Form()
        self.research_result_ui.setupUi(self.research_result)
        self.research_result.show()

    def print_roots(self, roots, accuracy):
        output_message = f'\nЗаданная точность: {accuracy}' \
                         f'\nНайденные корни:\n'
        for root in roots:
            output_message += f'{root}\n'

        self.result_label.setText(output_message)

    def finding_roots(self):
        CHORD_METHOD = "chord"
        BINARY_METHOD = "binary"

        with open("data/settings_data.json", "r") as file:
            settings_data = json.load(file)

        with open("data/intervals_data.json", "r") as file:
            intervals_data = json.load(file)

        def define_function(inp_str):
            equal_sign_index = inp_str.find("=")
            if equal_sign_index != -1:
                left_expr = slv.sympify(inp_str[:equal_sign_index])
                right_expr = slv.sympify(inp_str[equal_sign_index + 1:])
                func = left_expr - right_expr
                return func

            return slv.sympify(inp_str)

        def find_equation_roots(intervals, method, safe_mode, eps):
            if method == CHORD_METHOD:
                finding_method = slv.the_chord_method
            elif method == BINARY_METHOD:
                finding_method = slv.the_binary_method

            roots = []
            iteration_sum = 0
            for beg, end in intervals:
                current_root, current_iteration_number = finding_method(func, beg, end, safe_mode, eps)
                roots.append(current_root)
                iteration_sum += current_iteration_number
            return [roots, iteration_sum]

        def define_intervals(func, is_find_interval_mode):
            if is_find_interval_mode:
                interval_beg = settings_data["general"]["left_interval"]
                interval_end = settings_data["general"]["right_interval"]
                intervals_with_roots = slv.find_intervals_with_root(func, interval_beg, interval_end)
                is_safe_intervals = True
            else:
                intervals_with_roots = intervals_data["intervals"]
                is_safe_intervals = False
            return intervals_with_roots, is_safe_intervals

        def simple_finding(func, find_intervals=True):
            intervals_with_roots, is_safe_intervals = define_intervals(func, find_intervals)

            PRECISION_POINT = settings_data["general"]["accuracy"]
            equation_roots = find_equation_roots(intervals_with_roots, method=CHORD_METHOD,
                                                 safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT))[0]
            return equation_roots, PRECISION_POINT

        def comparing_finding(func, find_intervals=True):
            intervals_with_roots, is_safe_intervals = define_intervals(func, find_intervals)

            PRECISION_POINT_1 = settings_data["comparing"]["first_accuracy"]
            PRECISION_POINT_2 = settings_data["comparing"]["second_accuracy"]
            PRECISION_POINT_3 = settings_data["comparing"]["third_accuracy"]

            equations_roots_by_chord = []
            chord_iterations_number = []
            equations_roots_by_binary = []
            binary_iterations_number = []

            MAX_ACCURACY = max(PRECISION_POINT_1, PRECISION_POINT_2, PRECISION_POINT_3)
            if PRECISION_POINT_1 != "":
                roots, iteration_num = find_equation_roots(intervals_with_roots, method=CHORD_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_1))
                equations_roots_by_chord.append(roots)
                chord_iterations_number.append(iteration_num)

                if PRECISION_POINT_1 == MAX_ACCURACY:
                    current_result_roots = roots

                roots, iteration_num = find_equation_roots(intervals_with_roots, method=BINARY_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_1))
                equations_roots_by_binary.append(roots)
                binary_iterations_number.append(iteration_num)

            if PRECISION_POINT_2 != "":
                roots, iteration_num = find_equation_roots(intervals_with_roots, method=CHORD_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_2))
                equations_roots_by_chord.append(roots)
                chord_iterations_number.append(iteration_num)

                if PRECISION_POINT_2 == MAX_ACCURACY:
                    current_result_roots = roots

                roots, iteration_num = find_equation_roots(intervals_with_roots, method=BINARY_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_2))
                equations_roots_by_binary.append(roots)
                binary_iterations_number.append(iteration_num)

            if PRECISION_POINT_3 != "":
                roots, iteration_num = find_equation_roots(intervals_with_roots, method=CHORD_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_3))
                equations_roots_by_chord.append(roots)
                chord_iterations_number.append(iteration_num)

                if PRECISION_POINT_3 == MAX_ACCURACY:
                    current_result_roots = roots

                roots, iteration_num = find_equation_roots(intervals_with_roots, method=BINARY_METHOD,
                                                           safe_mode=is_safe_intervals, eps=10 ** (-PRECISION_POINT_3))
                equations_roots_by_binary.append(roots)
                binary_iterations_number.append(iteration_num)

            self.save_research_result(settings_data["comparing"], chord_iterations_number, binary_iterations_number)

            return current_result_roots, MAX_ACCURACY

        input_expr = self.input_equation.text()

        func = define_function(input_expr)
        is_find_intervals = len(intervals_data["intervals"]) == 0

        if self.compare_method_ckbx.isChecked():
            equation_roots, accuracy = comparing_finding(func, is_find_intervals)
            self.show_research_result()
            self.output_result(func, equation_roots, accuracy)
        else:
            equation_roots, accuracy = simple_finding(func, is_find_intervals)
            self.output_result(func, equation_roots, accuracy)

    def show_graph(self, func, roots):
        MIN_DOMAIN = 20

        def define_interval(roots):
            beg = roots[0]
            end = roots[-1]
            if end - beg == 0:
                beg -= MIN_DOMAIN
                end += MIN_DOMAIN
            else:
                step = abs(end - beg) / 5
                beg -= step
                end += step
            return beg, end

        BEG, END = define_interval(roots)
        STEP = 0.03
        MAIN_INTERVAL_POINTS_NUM = int((END - BEG) / STEP)
        ALL_POINTS_NUM = 10 ** 3

        f = lambda arg: float(slv.eval_func(func, arg))

        # todo Проверять точки на действительность
        GRAPH_BEGIN = BEG - ALL_POINTS_NUM / 2 * STEP
        x_array = [GRAPH_BEGIN + i * STEP for i in range(MAIN_INTERVAL_POINTS_NUM + ALL_POINTS_NUM)]
        l = f(x_array[0])
        y_array = [f(x) for x in x_array]
        self.graph_view.plot(x_array, y_array, pen="b")

        # self.graph_view.plot([-10 ** 14, 10 ** 14], [0, 0], pen="w")

        HALF_OF_DOMAIN = abs(END - BEG) / 2
        self.graph_view.setXRange(BEG, END, 0)
        self.graph_view.setYRange(-HALF_OF_DOMAIN, HALF_OF_DOMAIN, 0)

        self.graph_view.showGrid(x=True, y=True, alpha=0.3)

        # todo Правильно расставить метки
        for root in roots:
            self.graph_view.plot([root], [0], pen=None, symbol="o", symbolBrush="red", symbolPen="red")
            item = pyqtgraph.TextItem(str(root))
            self.graph_view.addItem(item)

    def clear_graph(self):
        self.graph_view.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
