from random import randint
import user_interface as ui


def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)


def get_pressure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)


def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 40)


def data_collection(sensor=1):
    return (ui.temperature_view(sensor), ui.pressure_view(sensor), ui.wind_speed_view(sensor))
