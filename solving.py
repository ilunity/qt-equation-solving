from builtins import max

from sympy import *
import numexpr

X_ARG = Symbol("x")
MAX_CHORD_ITERATION_NUMBER = 150
MAX_DOMAIN_LENGTH = 30
PRECISION_AFTER_DECIMAL_POINT = 3


def remove_extreme_points(function, beg, end):
    interval = [beg, end]
    second_derivative_of_func = derivative(function)

    for i in range(2):
        param = interval[i]
        iter = abs(end - beg) / 10
        iter = iter * (-1) if i == 1 else iter  # adding for left and subtracting fo right
        while eval_func(second_derivative_of_func, param) == 0:
            new_param = param + iter
            if eval_func(function, param) * eval_func(function, new_param) < 0:
                iter /= 10
                continue
            param = new_param
        interval[i] = param

    return interval


def minimize_interval(function, beg, end):
    interval = [beg, end]

    for i in range(2):
        iter = abs(end - beg) / 2
        iter = iter * (-1) if i == 1 else iter  # adding for left and subtracting fo right
        while iter > 5 and abs(interval[0] - interval[1]) > MAX_DOMAIN_LENGTH:
            new_param = interval[i] + iter
            if eval_func(function, interval[i]) * eval_func(function, new_param) < 0:
                iter /= 2
                continue
            interval[i] = new_param

    return interval


# todo: добавить проверки на действительные числа. Пока что функция должная быть определена на отрезке [interval_begin, interval_end]
def filter_intervals_with_roots(function, possible_points_set, interval_begin, interval_end):
    intervals_with_roots = []
    last_param = interval_begin
    last_value = eval_func(function, interval_begin)

    for param in possible_points_set:
        value = eval_func(function, param)
        if value * last_value < 0:
            # intervals_with_roots.append([last_param.evalf(), param.evalf()])
            if param - last_param > MAX_DOMAIN_LENGTH:
                last_param, param = minimize_interval(function, last_param, param)
            intervals_with_roots.append([x.evalf() for x in remove_extreme_points(function, last_param, param)])

        elif value == 0:
            intervals_with_roots.append([param.evalf(), param.evalf()])

        last_param, last_value = param, value

    value = eval_func(function, interval_end)
    if value * last_value < 0:
        # intervals_with_roots.append([last_param.evalf(), interval_end])
        intervals_with_roots.append([x.evalf() for x in remove_extreme_points(function, last_param, interval_end)])

    elif value == 0:
        intervals_with_roots.append([interval_end, interval_end])

    return intervals_with_roots


def filter_intervals_by_second_der(function, input_intervals):
    second_derivative_of_func = derivative(function, 2)
    special_points = solveset(second_derivative_of_func, X_ARG)

    intervals_with_root = []
    for beg, end in input_intervals:
        interval = Interval(beg, end)

        possible_points_set = interval.intersect(special_points)
        if possible_points_set.is_empty:
            intervals_with_root.append([beg, end])
        else:
            intervals_with_root.extend(filter_intervals_with_roots(function, possible_points_set, beg, end))

    return intervals_with_root


# Функция должная быть определена на отрезке [interval_begin, interval_end]
def find_intervals_with_root(function, interval_begin=-100, interval_end=100):
    derivative_of_func = derivative(function)
    special_points_set = solveset(derivative_of_func, X_ARG)

    if special_points_set.is_empty:
        if eval_func(function, interval_begin) * eval_func(function, interval_end) < 0:
            return [[interval_begin, interval_end]]

    interval_begin = Float(interval_begin)
    interval_end = Float(interval_end)
    interval = Interval(interval_begin, interval_end)
    special_points_set = interval.intersect(special_points_set)

    intervals_with_root = filter_intervals_with_roots(function, special_points_set, interval_begin, interval_end)

    return filter_intervals_by_second_der(function, intervals_with_root)


def eval_func(func, arg):
    return round(func.evalf(subs={X_ARG: arg}), 14)

def derivative(function, rank=1):
    for i in range(rank):
        function = function.diff()
    return function


def identify_points(function, beg, end):
    func_der_2 = derivative(function, 2)

    average_point = beg + (end - beg) / 2

    if eval_func(function, beg) * eval_func(func_der_2, average_point) > 0:
        return [beg, end]

    if eval_func(function, end) * eval_func(func_der_2, average_point) > 0:
        return [end, beg]


def infimum(func, a, b):
    func = sqrt(func ** 2)
    return minimum(func, X_ARG, Interval(a, b))


def supremum(func, a, b):
    func = sqrt(func ** 2)
    return maximum(func, X_ARG, Interval(a, b))


def accuracy_achieved_func(m, M):
    if M <= 2 * m:
        def accuracy_func(next_x, prev_x, eps):
            return abs(next_x - prev_x) < eps
    else:
        if m == 0:
            m = 10 ** (-10)

        def accuracy_func(next_x, prev_x, eps):
            return (M - m) * abs(next_x - prev_x) < eps * m

    return accuracy_func


def next_point(func, prev_x, fixed_x):
    return (prev_x - (fixed_x - prev_x) * eval_func(func, prev_x) /
            (eval_func(func, fixed_x) - eval_func(func, prev_x)))


def is_convergence_condition_satisfied(function, beg, end):
    second_derivative_of_func = derivative(function, 2)

    if beg * end > 0:
        return False
    if find_intervals_with_root(second_derivative_of_func) > 0:
        return False
    if not is_defined_function(function, beg, end):
        return False

    return True


def is_defined_function(function, beg, end):
    iter = (end - beg)/100
    argument = beg
    for i in range(100):
        value = eval_func(function, argument)
        if value.is_complex:
            return False
        argument += iter
    return True

def the_chord_method(function, beg, end, safe_mode=False, eps=10 ** (-PRECISION_AFTER_DECIMAL_POINT)):
    if not safe_mode:
        if not is_convergence_condition_satisfied(function, beg, end):
            return False

    fixed_x, previous_x = identify_points(function, beg, end)
    if beg == end:
        return [beg, 0]

    m = infimum(function.diff(), beg, end)
    M = supremum(function.diff(), beg, end)

    is_accuracy_achieved = accuracy_achieved_func(m, M)

    iteration_number = 0
    while iteration_number < MAX_CHORD_ITERATION_NUMBER:
        iteration_number += 1
        next_x = next_point(function, previous_x, fixed_x)
        if is_accuracy_achieved(next_x, previous_x, eps):
            return [next_x, iteration_number]
        previous_x = next_x

    return False
# todo Исправить принятие информации в main

def the_binary_method(function, beg, end, safe_mode=False, eps=10 ** (-PRECISION_AFTER_DECIMAL_POINT)):
    if not safe_mode:
        if not is_defined_function(function, beg, end):
            return False
        if beg * end > 0:
            return False

    start = beg
    final = end

    iter = 0
    while (end - beg) / (2 ** iter) > eps:
        pivot = (start + final) / 2.0
        if eval_func(function, start) * eval_func(function, pivot) < 0:
            final = pivot
        else:
            start = pivot
        iter += 1
    return [start, iter]


if __name__ == "__main__":
    # f = sympify(input('Input function with "x" argument: '))
    # f = X_ARG + cos(X_ARG) - 2
    f = X_ARG**(1/2)
    # f_str = "x**(1/2)"
    print(is_defined_function(f, -1, 5))
    a, b = find_intervals_with_root(f)[0]
    print('The first finding root: ' + the_chord_method(f, a, b)[0])
