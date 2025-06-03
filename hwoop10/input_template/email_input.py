from input_template import InputTemplate


class EmailInput(InputTemplate):
    def prompt(self):
        return "Enter your email address"

    def custom_validation(self, value):
        return (
                "@" in value and
                len(value.split("@")[0]) > 0 and
                len(value.split("@")[1]) > 0
        )
