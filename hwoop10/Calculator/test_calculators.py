from calculator import Calculator
from free_calculator_proxy import FreeCalculatorProxy

if __name__ == "__main__":
    full_calc = Calculator()
    free_calc = FreeCalculatorProxy()

    print("Full Calculator: 2 ** 3 =", full_calc.pow(2, 3))
    print("Free Calculator: 5 + 3 =", free_calc.add(5, 3))
    print("Free Calculator: 5 - 2 =", free_calc.sub(5, 2))

    try:
        print("Free Calculator: 2 ** 3 =", free_calc.pow(2, 3))
    except PermissionError as e:
        print("PermissionError:", e)