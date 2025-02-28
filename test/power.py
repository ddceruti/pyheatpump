import pytest
from pyheatpump import power

# Default values
REINJECTION_TEMPERATURE = 40  # deg. C
NETWORK_TEMPERATURE = 90  # deg. C
GEOTHERMAL_SUPPLY_TEMPERATURE = 70  # deg. C
MASS_FLOW = 100.0  # kg/s


def test_calculate_thermal_power():
    available_power = power.calculate_thermal_power(
        high_temperature=GEOTHERMAL_SUPPLY_TEMPERATURE,
        low_temperature=REINJECTION_TEMPERATURE,
        mass_flow=MASS_FLOW
    )
    expected_power = 12.56e6  # Expected value in Watts
    assert pytest.approx(available_power, rel=1e-2) == expected_power

def test_calculate_output_power():
    cop = 3.19  # Example COP value
    thermal_power_source = 12.56e6  # Example thermal power source in Watts
    total_power = power.calculate_output_power(
        cop=cop,
        thermal_power_source=thermal_power_source
    )
    expected_total_power = 16.50e6  # Expected value in Watts
    assert pytest.approx(total_power, rel=1e-2) == expected_total_power
