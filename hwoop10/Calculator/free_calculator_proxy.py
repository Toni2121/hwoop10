from calculator import Calculator

class FreeCalculatorProxy:
    def __init__(self):
        self._calculator = Calculator()

    def add(self, a, b):
        return self._calculator.add(a, b)

    def sub(self, a, b):
        return self._calculator.sub(a, b)

    def pow(self, a, b):
        raise PermissionError("Power operation is available only in the full version.")