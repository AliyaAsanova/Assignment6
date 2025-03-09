# Assignment6
# BMI Calculator

## Description
This is a simple BMI (Body Mass Index) Calculator built using PyQt6. It allows users to input their weight (in kilograms) and height (in meters) to calculate their BMI and determine their weight status.

## Features
- User-friendly graphical interface
- Input fields for weight and height
- Button to calculate BMI
- Displays BMI value and corresponding weight status
- Menu options to clear inputs and exit the application
- Help section with usage instructions

## Installation
### Prerequisites
Ensure you have Python installed on your system. You also need to install PyQt6 if it's not already installed.

```bash
pip install PyQt6
```

### Running the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bmi-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bmi-calculator
   ```
3. Run the application:
   ```bash
   python bmi_calculator.py
   ```

## Usage
1. Enter your weight in kilograms in the `Weight (kg)` input field.
2. Enter your height in meters in the `Height (m)` input field.
3. Click the **Calculate BMI** button.
4. The application will display your BMI value and weight status:
   - **Underweight** (BMI < 18.5)
   - **Normal weight** (BMI 18.5–24.9)
   - **Overweight** (BMI 25–29.9)
   - **Obese** (BMI ≥ 30)
5. To clear the inputs, use the **Clear** option from the `File` menu.
6. To exit, use the **Exit** option from the `File` menu.
7. For usage instructions, use the `Help > How to use` menu option.

## File Structure
```
/ bmi-calculator
   ├── bmi_calculator.py   # Main script containing the PyQt6 application
   ├── README.md           # Documentation file
```

## Sample Input/Output
### Sample Input
```
Weight: 70 kg
Height: 1.75 m
```

### Sample Output
```
BMI: 22.86
Status: Normal weight
```



