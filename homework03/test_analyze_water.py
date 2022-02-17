import pytest
import math
from analyze_water import create_new_list
from analyze_water import calculate_turbidity
from analyze_water import calculate_minimum_time

data_1 = {'a': 2.57, 'b': 4.62}
assert(calculate_turbidity(data_1, 'a', 'b') == 11.8734)

a = 0.75
b = 1.5
c = 0.5
assert(calculate_minimum_time(a, b, c) == 1)

data_2 = [1, 2, 3, 4, 5, 6, 7, 8]
assert(isinstance(create_new_list(data_2), list) == True)

assert(isinstance(calculate_turbidity(data, 'a', 'b'), float) == True)


