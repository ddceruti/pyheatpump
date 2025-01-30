"""This example demonstrates how to calculate the efficiency of a heat pump."""

from pyheatpump import cop


if __name__ == "__main__":
    delta_T = 20
    T_sink_out = 40
    print(f"Temperature of the heat sink outlet: {T_sink_out} deg. C")
    print(f"Temperature difference: {delta_T} K")
    
    cop.calculate(delta_T, T_sink_out)
    print(f"Conventional heat pump efficiency: {cop.calculate(delta_T, T_sink_out):.2f}")

    carnot = cop.carnot(delta_T, T_sink_out + 273.15, quality_factor=1)
    print(f"Carnot efficiency: {carnot:.2f}")
