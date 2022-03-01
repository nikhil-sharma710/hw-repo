import pytest
from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes

def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')

def test_check_hemisphere():
    assert check_hemisphere(1, 1) == 'Northern & Eastern'
    assert check_hemisphere(1, -1) == 'Northern & Western'
    assert check_hemisphere(-1, 1) == 'Southern & Eastern'
    assert check_hemisphere(-1, -1) == 'Southern & Western'
    assert isinstance(check_hemisphere(2, -4), str) == True

def test_count_classes():
    assert count_classes([{'a': 'b'}], 'a') == {'b': 1}
    assert count_classes([{'a': 'b'}, {'a': 'c'}], 'a') == {'b': 1, 'c': 1}
    assert count_classes([{'a': 'b'}, {'a': 'b'}, {'a': 'c'}], 'a') == {'b': 2, 'c': 1}
    assert isinstance(count_classes([{'a': 'b'}, {'a': 'c'}], 'a'), dict) == True

    with pytest.raises(KeyError):
        count_classes([{'a': 'b'}, {'c': 'b'}], 'a')

def main():
    test_compute_average_mass()
    test_check_hemisphere()
    test_count_classes()

if __name__ == "__main__":
    main()
