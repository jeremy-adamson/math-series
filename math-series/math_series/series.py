
def fibonacci(n):
    """
    Seeds the recursive function with fibonacci base values
    :param n: the nth term to be found in a fibonacci sequence
    :return: the nth term of a fibonacci sequence
    """
    calc_values = {0:0, 1:1}
    return sum_series_recurse(n, calc_values)

def lucas(n):
    """
    Seeds the recursive function with lucas base values
    :param n: the nth term to be found in a lucas sequence
    :return: the nth term of a lucas sequence
    """
    calc_values = {0:2, 1:1}
    return sum_series_recurse(n, calc_values)

def sum_series(n, base1 = 0, base2 = 1):
    """
    Seeds the recursive function with user defined base values (defaults provided)
    :param n: the nth term to be found in a generic summation sequence
    :param base1 = the 1st generic base term for a summation
    :param base2 = the 2nd generic base term for a summation
    :return: the nth term of the generic summation sequence given two base values (fibonacci as default)
    """
    calc_values = {0:base1, 1:base2}
    return sum_series_recurse(n, calc_values)

def sum_series_recurse(n, calc_values):
    """
    Recursive function with memoization for calculating a summation sequence
    :param n: the nth term to be found in the summation sequence
    :param calc_values: dictionary of calculated values seeded with the base terms
    :return: the nth term of the generic summation sequence based upon the initial calc_values entries
    """
    if n < 0:
        return None
    if n in calc_values.keys():
        print(calc_values)
        return calc_values[n]

    new_value = sum_series_recurse(n - 1, calc_values) + sum_series_recurse(n - 2, calc_values)
    calc_values.update({n:new_value})
    return new_value