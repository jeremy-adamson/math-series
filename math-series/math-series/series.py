
def fibonacci(n):
    calc_values = {0:0, 1:1}
    return sum_series_recurse(n, calc_values)

def lucas(n):
    calc_values = {0:2, 1:1}
    return sum_series_recurse(n, calc_values)

def sum_series(n, base1 = 0, base2 = 1):
    calc_values = {0:base1, 1:base2}
    return sum_series_recurse(n, calc_values)

def sum_series_recurse(n, calc_values):
    if n in calc_values.keys():
        return calc_values[n]

    new_value = sum_series_recurse(n - 1, calc_values) + sum_series_recurse(n - 2, calc_values)
    calc_values.update({n:new_value})
    return new_value