from series import fibonacci
from series import lucas
from series import sum_series

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
    actual = lucas(11)
    expected = 199
    assert actual == expected

def test_luc3():
    actual = lucas(21)
    expected = 24476
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
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_series2():
    actual = sum_series(3, 2, 4)
    expected = 10
    assert actual == expected

def test_series3():
    actual = sum_series(3, 10, 11)
    expected = 32
    assert actual == expected
