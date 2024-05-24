- IndoorTemperature, OutdoorTemperature

    Cold: Open left (b = 20, c = 25)

    Medium: Triangular (a = 20, b = 25, c = 30)

    Hot: Open right (a = 25, b = 30)

- Fan speed

    Zero: Triangular(a = -150, b = 0, c = 150)

    Slow: Triangular(a = 0, b = 150, c = 300)

    Medium: Triangular(a = 150, b = 300, c = 450)

    Fast: Triangular(a = 300, b = 450, c = 600)

    Max: Triangular(a = 450, b = 600, c = 750)

- Fuzzy rules

    R1: if IndoorTemperature is Cold and OutdoorTemperature is Cold then FanSpeed is Zero

    R2: if IndoorTemperature is Medium and OutdoorTemperature is Cold then FanSpeed is Slow

    R3: if IndoorTemperature is Hot and OutdoorTemperature is Cold then FanSpeed is Medium

    R4: if IndoorTemperature is Cold and OutdoorTemperature is Medium then FanSpeed is Slow

    R5: if IndoorTemperature is Medium and OutdoorTemperature is Medium then FanSpeed is Medium

    R6: if IndoorTemperature is Hot and OutdoorTemperature is Medium then FanSpeed is Fast

    R7: if IndoorTemperature is Cold and OutdoorTemperature is Hot then FanSpeed is Medium

    R8: if IndoorTemperature is Medium and OutdoorTemperature is Hot then FanSpeed is Fast
    
    R9: if IndoorTemperature is Hot and OutdoorTemperature is Hot then FanSpeed is Max