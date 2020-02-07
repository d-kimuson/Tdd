import pytest

from main import FizzBuzz


@pytest.fixture
def fizzbuzz():
    return FizzBuzz()


class T_3の倍数:
    def case_3を渡したらFizzを返す(self, fizzbuzz):
        assert fizzbuzz.convert(3) == "Fizz"


class T_5の倍数:
    def case_5を渡したらBuzzを返す(self, fizzbuzz):
        assert fizzbuzz.convert(5) == "Buzz"


class T_15の倍数:
    def case_15を渡したらFizzBuzzを返す(self, fizzbuzz):
        assert fizzbuzz.convert(15) == "FizzBuzz"


class T_その他:
    def case_1を渡したら文字列1を返す(self, fizzbuzz):
        assert fizzbuzz.convert(1) == "1"

    def case_2を渡したら文字列2を返す(self, fizzbuzz):
        assert fizzbuzz.convert(2) == "2"
