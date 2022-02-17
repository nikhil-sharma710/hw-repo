import pytest
import math
from analyze_water import create_new_list
from analyze_water import calculate_turbidity
from analyze_water import calculate_minimum_time

def test_calculate_turbidity():
    data_1 = {'a': 2.57, 'b': 4.62}
    
    assert(calculate_turbidity(data_1, 'a', 'b') == 11.8734)
    assert(isinstance(calculate_turbidity(data, 'a', 'b'), float) == True)

def test_calculate_minimum_time():
    a = 0.75
    b = 1.5
    c = 0.5
    
    assert(calculate_minimum_time(a, b, c) == 1)
    
    with pytest.raises(TypeError):
        calculate_minimum_time('a', b, c)
        
 def main():
     test_calculate_turbidity()
     test_calculate_minimum_time()
 
if __name__ == '__main__':
    main()
