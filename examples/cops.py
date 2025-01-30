import hp.cop as cop

if __name__ == "__main__":
    delta_T = 20
    T_sink_out = 40
    print(f"Temperature of the heat sink outlet: {T_sink_out} °C")
    print(f"Temperature difference: {delta_T} K")
    
    cop.carnot(delta_T, T_sink_out)
    cop.calculate(delta_T, T_sink_out)

    print(f"Carnot efficiency: {cop.carnot(delta_T, T_sink_out)}")
