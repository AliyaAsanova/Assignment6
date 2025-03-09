import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, 
                              QVBoxLayout, QWidget, QMenuBar, QMessageBox, QHBoxLayout)
from PyQt6.QtGui import QFont, QAction

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 300)
        
        # Create input fields
        self.weight_label = QLabel("Weight (kg):", self)
        self.weight_label.setFont(QFont("Arial", 10))
        self.weight_input = QLineEdit(self)
        
        self.height_label = QLabel("Height (cm):", self)
        self.height_label.setFont(QFont("Arial", 10))
        self.height_input = QLineEdit(self)
        
        # Calculate Button
        self.calculate_button = QPushButton("Calculate BMI", self)
        self.calculate_button.setFont(QFont("Arial", 10, weight=QFont.Weight.Bold))
        self.calculate_button.clicked.connect(self.calculate_bmi)
        
        # Result Label
        self.result_label = QLabel("Your BMI:", self)
        self.result_label.setFont(QFont("Arial", 12, weight=QFont.Weight.Bold))
        self.result_label.setStyleSheet("background-color: green; color: white; padding: 5px;")
        
        # Layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.weight_label)
        input_layout.addWidget(self.weight_input)
        input_layout.addWidget(self.height_label)
        input_layout.addWidget(self.height_input)
        input_layout.addWidget(self.calculate_button)
        input_layout.addWidget(self.result_label)
        
        container = QWidget()
        container.setLayout(input_layout)
        self.setCentralWidget(container)
        
        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        help_menu = menubar.addMenu("Help")
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        file_menu.addAction(clear_action)
        
        help_action = QAction("How to Use", self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100  # Convert cm to meters
            bmi = weight / (height ** 2)
            status = self.get_bmi_status(bmi)
            
            # Change background color based on BMI category
            color = "green" if 18.5 <= bmi < 25 else "orange" if 25 <= bmi < 30 else "red" if bmi >= 30 else "yellow"
            self.result_label.setStyleSheet(f"background-color: {color}; color: white; padding: 5px;")
            
            self.result_label.setText(f"Your BMI: {bmi:.2f} ({status})")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numerical values for weight and height.")
    
    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("Your BMI:")
        self.result_label.setStyleSheet("background-color: green; color: white; padding: 5px;")
    
    def show_help(self):
        QMessageBox.information(self, "How to Use", "Enter your weight in kg and height in cm, then press 'Calculate BMI' to see your result.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
