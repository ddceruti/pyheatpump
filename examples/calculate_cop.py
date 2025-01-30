"""This example demonstrates how to calculate the efficiency of a heat pump."""

from pyheatpump import cop


if __name__ == "__main__":
    source_temperature = 20
    sink_temperature = 60
    delta = sink_temperature - source_temperature
    print(f"Temperature of the heat sink outlet: {sink_temperature} deg. C")
    print(f"Temperature difference: {delta} K")
    
    conv = cop.calculate(source_temperature=source_temperature,
                         sink_temperature=sink_temperature)
    print(f"Conventional heat pump efficiency: {conv:.2f}")

    carnot = cop.carnot(delta, sink_temperature + 273.15, quality_factor=1)
    print(f"Carnot efficiency: {carnot:.2f}")
