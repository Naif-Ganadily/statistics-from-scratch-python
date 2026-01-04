import pytest
from statsfs.descriptive.central_tendency import mean
from statsfs.descriptive.central_tendency import median
from statsfs.descriptive.central_tendency import midrange

# Mean Unit Tests:
def test_mean_integers():
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_floats():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_mixed():
    assert mean([1, 2.5, 3]) == pytest.approx(2.1666666667)


def test_mean_empty():
    with pytest.raises(ValueError, match="Empty"):
        mean([])


def test_mean_non_numeric():
    with pytest.raises(TypeError, match="Non-numeric"):
        mean(["Naif", "Yash", 5])

# Median Unit Tests:
        
def test_median_integers():
    assert median([1, 2, 3, 4, 5]) == 3

def test_median_floats():
    assert median([1.0, 2.0, 3.0]) == 2.0

def test_median_mixed():
    assert median([0.3, 1, 2.5, 3, 4.6]) == 2.5

def test_median_empty():
    with pytest.raises(ValueError, match="Empty"):
        median([])

def test_median_non_numeric():
    with pytest.raises(TypeError, match="Non-numeric"):
        median(["Naif", "Yash", 5])

# Midrange Unit Tests:
        
def test_midrange_integers():
    assert midrange([1, 2, 3, 4, 5]) == 3

def test_midrange_floats():
    assert midrange([1.0, 2.0, 3.0]) == 2.0

def test_midrange_mixed():
    assert midrange([1.5, 4, 2.5, 3, 10.5]) == 6

def test_midrange_non_numeric():
    with pytest.raises(TypeError, match="Non-numeric"):
        midrange(["Naif", "Yash", 5])