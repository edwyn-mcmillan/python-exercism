""" Meltdown Mitigation exercise """


def is_criticality_balanced(temperature, neutrons_emitted):
    return bool(temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    real_percentage = efficiency_percentage(voltage, current, theoretical_max_power)

    if real_percentage >= 80:
        return 'green'
    if(real_percentage < 80 and real_percentage >= 60):
        return 'orange'
    if(real_percentage < 60 and real_percentage >= 30):
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    current_reading = temperature * neutrons_produced_per_second
    if current_reading < (threshold * 0.9):
        return 'LOW'
    elif current_reading >= (threshold - (threshold * 0.1)) and current_reading <= (threshold + (threshold * 0.1)):
        return 'NORMAL'
    else:
        return 'DANGER'


def efficiency_percentage(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    return (generated_power / theoretical_max_power) * 100