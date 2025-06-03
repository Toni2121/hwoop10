from input_template import InputTemplate


class IntInput1to100(InputTemplate):
    def prompt(self):
        return "Enter a number between 1 and 100"

    def convert(self, input_str):
        return int(input_str)

    def custom_validation(self, value):
        return 1 <= value <= 100
