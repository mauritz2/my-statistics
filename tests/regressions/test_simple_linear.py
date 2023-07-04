import pytest
import pandas as pd
import matplotlib.pyplot as plt
from regressions.simple_linear import SimpleLinear

@pytest.fixture
def simple_linear():
    simple_linear = SimpleLinear()
    return simple_linear


def test_validate_x_y_valid(simple_linear):
    x = pd.Series([1, 2, 3])
    y = pd.Series([4, 5, 6])
    simple_linear.validate_x_y(x, y)


def test_validate_x_y_invalid(simple_linear):
    x = pd.Series([1, 2])
    y = pd.Series([4, 5, 6])
    with pytest.raises(ValueError):
        simple_linear.validate_x_y(x, y)


def test_fit_intercept_only(simple_linear):
    x = pd.Series([1, 2, 3])
    y = pd.Series([2, 3, 4])
    
    simple_linear.fit(x, y)

    assert simple_linear.b0 == 1.0
    assert simple_linear.b1 == 1.0


def test_fit_intercept_and_coefficient(simple_linear):
    x = pd.Series([1, 2, 3])
    y = pd.Series([3, 5, 7])
    
    simple_linear.fit(x, y)

    assert simple_linear.b0 == 1.0
    assert simple_linear.b1 == 2.0


def test_fit_negative_nums(simple_linear):
    x = pd.Series([-1, -2, -3])
    y = pd.Series([-3, -5, -7])
    
    simple_linear.fit(x, y)

    assert simple_linear.b0 == -1.0
    assert simple_linear.b1 == 2.0


def test_predict(simple_linear):
    x_train = pd.Series([1, 2, 3])
    y_train = pd.Series([3, 5, 7])
    prediction_expected = y_train

    simple_linear.fit(x_train, y_train)
    prediction = simple_linear.predict(x_train)
    assert (prediction == prediction_expected).all() == True

def test_predict_negative(simple_linear):
    x_train = pd.Series([-8, -6, -4])
    y_train = pd.Series([2, 4, 6])
    prediction_expected = y_train

    simple_linear.fit(x_train, y_train)
    prediction = simple_linear.predict(x_train)
    assert (prediction == prediction_expected).all() == True

