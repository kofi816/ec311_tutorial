# main.py
# EC311 GitHub demonstration

from sensor import (
    read_temperature,
    celsius_to_fahrenheit,
    check_alarm,
)


def main():
    temperature = read_temperature()

    print("=== Temperature Monitor ===")
    print(f"Temperature: {temperature} C")
    print(
        f"Fahrenheit: "
        f"{celsius_to_fahrenheit(temperature)} F"
    )

    if check_alarm(temperature):
        print("Status: HIGH TEMPERATURE!")
    else:
        print("Status: Normal")


if __name__ == "__main__":
    main()
