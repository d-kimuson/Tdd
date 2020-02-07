class FizzBuzz:
    def __init__(self):
        pass

    def convert(self, number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)


if __name__ == "__main__":
    pass
