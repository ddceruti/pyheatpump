"""Module for calculating the available power of a heat source
and the total thermal output power of a heat pump."""

# Hardcoded dictionary with heat pump parameters from paper
WATER = {
    "cp": 4.187e3,  # J/kg K
}


def calculate_thermal_power(
        high_temperature: float=70.,
        low_temperature: float=40.,
        mass_flow: float=100.) -> float:
    """Calculates the thermal power of a water heat source depending
    on the available mass flow and temperature drop.

    Args:
        high_temperature (float): Temperature of the heat source [K].
        low_temperature (float): Temperature of the heat sink [K].
        mass_flow (float): Mass flow rate of the working fluid [kg/s].
    
    Returns:
        float: Thermal power [W].

    The model is defined as:

    .. math::
        P_{thermal} [W] = c_p \cdot \dot{m} \cdot \Delta T
    """
    delta_T = high_temperature - low_temperature
    if delta_T < 0:
        raise ValueError(f"The temperature difference {high_temperature} - {low_temperature} must be positive.")
    
    if mass_flow < 0:
        raise ValueError(f"The mass flow rate {mass_flow} must be positive.")

    heat_capacity = WATER["cp"] * mass_flow
    thermal_power = heat_capacity * delta_T
    return thermal_power


def calculate_output_power(
        cop: float=3.,
        thermal_power_source: float=10.) -> float:
    """Calculate the total thermal power output of a heat pump.

    Args:
        cop (float): Coefficient of performance of the heat pump.
        thermal_power_source (float): Available thermal power of the heat source [W].

    Returns:
        float: Total thermal power [W].
    
    The model is defined as:

    .. math::
        P_{total} [W] = \\frac{1+\text{COP}}{\text{COP}} \cdot P_{thermal}
    """
    if cop < 0:
        raise ValueError(f"The coefficient of performance {cop} must be positive.")
    
    if thermal_power_source < 0:
        raise ValueError(f"The thermal power source {thermal_power_source} must be positive.")

    total_power = (1 + cop) * thermal_power_source / cop
    return total_power
