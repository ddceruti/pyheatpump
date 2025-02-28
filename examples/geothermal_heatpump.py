"""This example demonstrates how to calculate the efficiency of a heat pump."""

from pyheatpump import cop
from pyheatpump import power
from pyheatpump import costs


# temperature of the geothermal source when it is reinjected
REINJECTION_TEMPERATURE = 40  # deg. C
# temperature of the heat sink
NETWORK_TEMPERATURE = 90  # deg. C, 
# temperature of the geothermal source when it is extracted
GEOTHERMAL_SUPPLY_TEMPERATURE = 70  # deg. C


if __name__ == "__main__":
    # calculate the coefficient of performance of the heat pump
    delta = NETWORK_TEMPERATURE - REINJECTION_TEMPERATURE
    print(f"Temperature of the heat sink outlet: {NETWORK_TEMPERATURE} deg. C")
    print(f"Temperature difference: {delta} K")
    
    conv = cop.calculate(source_temperature=REINJECTION_TEMPERATURE,
                         sink_temperature=NETWORK_TEMPERATURE)
    print(f"Conventional heat pump efficiency: {conv:.2f}")

    carnot = cop.carnot(delta,
                        NETWORK_TEMPERATURE + 273.15,
                        quality_factor=1)
    print(f"Carnot efficiency: {carnot:.2f}")

    # calculate the maximum thermal power that can be extracted from the
    # geothermal source
    available_power = power.calculate_thermal_power(
        high_temperature=GEOTHERMAL_SUPPLY_TEMPERATURE,
        low_temperature=REINJECTION_TEMPERATURE,
        mass_flow=100.)
    print(f"Available geothermal thermal power: {available_power/1e6:.2f} W")

    # calculate the total thermal power output of the heat pump
    total_power = power.calculate_output_power(
        cop=conv,
        thermal_power_source=available_power)
    print(f"Total thermal power output: {total_power/1e6:.2f} W")

    electrical_power = total_power/conv
    print(f"Electrical power input: {electrical_power/1e6:.2f} MW")

    # calculate the cost of the heat pump (default is the cost of the heat pump
    # according to the Danish Energy Agency in reference to the total thermal
    # power output)
    cost = costs.interpolate(size=total_power/1e6)
    print(f"Cost of the heat pump: {cost:.2f} EUR")
