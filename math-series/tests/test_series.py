from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fib1():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib2():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fib3():
    actual = fibonacci(100)
    expected = 354224848179261915075
    assert actual == expected

def test_fib4():
    actual = fibonacci(30)
    expected = 832040
    assert actual == expected

def test_fib5():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_luc1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_luc2():
    actual = lucas(11.0)
    expected = 199
    assert actual == expected

def test_luc3():
    actual = lucas(21.4)
    expected = None
    assert actual == expected

def test_luc4():
    actual = lucas(36)
    expected = 33385282
    assert actual == expected

def test_luc5():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_series1():
    actual = sum_series('a')
    expected = None
    assert actual == expected

def test_series2():
    actual = sum_series(-3, 2, 4)
    expected = None
    assert actual == expected

def test_series3():
    actual = sum_series(3, 10, 11)
    expected = 32
    assert actual == expected

def test_series4():
    actual = sum_series(1, 10, 11)
    expected = 11
    assert actual == expected

def test_series5():
    actual = sum_series(0, 10, 11)
    expected = 10
    assert actual == expected
