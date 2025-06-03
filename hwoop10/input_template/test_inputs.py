from int_input_1to100 import IntInput1to100
from email_input import EmailInput

if __name__ == "__main__":
    print("---- Number Input ----")
    number = IntInput1to100().run()
    print("You entered:", number)

    print("\n---- Email Input ----")
    email = EmailInput().run()
    print("You entered:", email)