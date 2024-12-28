# Any pytest files should start with test_ or end with _test
# python method method name should start with test
# any code should be wrapped in method
import pytest


def test_firstprogram(): #for pytest u have to write your code under function only , wich called as modules for pytest .
    print("hello")

@pytest.mark.smoke
def test_secondprogram():
    print("good")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])



