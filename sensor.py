# sensor.py
# Simulated temperature sensor


def read_temperature():
    """Return a simulated temperature in Celsius."""
    return 25.0


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def check_alarm(temperature, threshold=30):
    """Check whether temperature exceeds the threshold."""
    return temperature > threshold


