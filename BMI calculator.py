import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMenuBar
from PyQt6.QtGui import QAction

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 300)

        # Центральный виджет и основной макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Поля ввода
        self.form_layout = QHBoxLayout()
        self.result_layout = QVBoxLayout()

        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # Метки результатов
        self.bmi_result_label = QLabel("BMI: ")
        self.bmi_status_label = QLabel("Status: ")

        # Добавление виджетов в макеты
        self.form_layout.addWidget(self.weight_label)
        self.form_layout.addWidget(self.weight_input)
        self.form_layout.addWidget(self.height_label)
        self.form_layout.addWidget(self.height_input)
        self.form_layout.addWidget(self.calculate_button)

        self.result_layout.addWidget(self.bmi_result_label)
        self.result_layout.addWidget(self.bmi_status_label)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.result_layout)

        # Добавление меню
        self.menu_bar = self.menuBar()
        self.create_menu()

    def create_menu(self):
        file_menu = self.menu_bar.addMenu("File")
        help_menu = self.menu_bar.addMenu("Help")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_inputs)

        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)

        help_action = QAction("How to use", self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            bmi = weight / (height ** 2)

            self.bmi_result_label.setText(f"BMI: {bmi:.2f}")
            self.bmi_status_label.setText(self.get_bmi_status(bmi))

        except ValueError:
            self.bmi_result_label.setText("Invalid input!")
            self.bmi_status_label.setText("Please enter valid numbers.")

    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Status: Underweight"
        elif 18.5 <= bmi < 25:
            return "Status: Normal weight"
        elif 25 <= bmi < 30:
            return "Status: Overweight"
        else:
            return "Status: Obese"

    def clear_inputs(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_result_label.setText("BMI: ")
        self.bmi_status_label.setText("Status: ")

    def show_help(self):
        help_message = (
            "Enter your weight in kilograms and height in meters.\n"
            "Click 'Calculate BMI' to calculate your Body Mass Index (BMI).\n"
            "The BMI status will indicate whether you are underweight, normal weight, overweight, or obese."
        )
        self.bmi_result_label.setText(help_message)
        self.bmi_status_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
