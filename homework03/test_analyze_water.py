import json
from analyze_water import calculate_turbidity
from analyze_water import calculate_minimum_time

data = {'a': 2, 'b': 4}
assert(calculate_turbidity(data, 'a', 'b') == 8)
