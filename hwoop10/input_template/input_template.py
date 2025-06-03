class InputTemplate:
    def run(self):
        while True:
            print(self.prompt())
            user_input = input("> ")

            if not user_input.strip():
                print("Input cannot be empty.")
                continue

            try:
                value = self.convert(user_input)
            except Exception as e:
                print("Invalid input format.")
                continue

            if not self.custom_validation(value):
                print("Input did not pass validation.")
                continue

            return value

    def prompt(self):
        raise NotImplementedError

    def convert(self, input_str):
        return input_str

    def custom_validation(self, value):
        return True