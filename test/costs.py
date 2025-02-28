import pytest
from pyheatpump import costs


def test_interpolate_cost():
    size = 16.50  # Example size in MW
    cost = costs.interpolate(size=size)
    expected_cost = 579977.87  # Example expected cost in EUR (replace with actual expected value)
    assert pytest.approx(cost, rel=1e-2) == expected_cost
