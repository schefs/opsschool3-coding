from weather import Weather, Unit

import click


def get_weather_object_temp_unit(weather):
    if weather.units.temperature == 'C':
        return 'Celsius'
    else:
        return 'Fahrenheit'


def get_weather_in_city(city, unit):
    weather = Weather(unit=getattr(Unit, unit))
    return weather.lookup_by_location(city)


def validate_days_requested_from_cli(forecast, weather):
    if forecast == 'TODAY':
        return True
    else:
        try:
            days = forecast.split('+')
            if days[0] == 'TODAY' and weather.forecast[int(days[1])]:
                return True
            raise ValueError('Syntax of days requested is not legal')
        except ValueError:
            raise ValueError('Syntax of days requested is not legal')
        except IndexError:
            raise IndexError("Forecast amount of days requested is not available")


def get_amount_of_days_requested_from_cli(forecast, weather):
    validate_days_requested_from_cli(forecast, weather)
    if forecast == 'TODAY':
        return 0
    else:
        return int(forecast.split('+')[1])


def print_today_weather_to_console(city, weather_condition, low_temp, high_temp, unit):
    print("The weather in {0} today is {1} with temperatures traling from {2}-{3} {4}\n"
          .format(city, weather_condition, low_temp, high_temp, unit))


def print_future_weather_to_console(date, weather_condition, low_temp, high_temp, unit):
    print("{0} {1} with temperatures traling from {2}-{3} {4}"
          .format(date, weather_condition, low_temp, high_temp, unit))


def print_forecast(days, weather):
    city = weather.location.city
    condition = weather.forecast[0].text
    low = weather.forecast[0].low
    high = weather.forecast[0].high
    unit = get_weather_object_temp_unit(weather)
    print_today_weather_to_console(city, condition, low, high, unit)
    if days != 0:
        print("Forecast for the next {0} days:".format(days))
        for day in range(days):
            condition = weather.forecast[day].text
            low = weather.forecast[day].low
            high = weather.forecast[day].high
            date = weather.forecast[day].date
            print_future_weather_to_console(date, condition, low, high, unit)


def validate_weather(weather):
    if not weather:
        raise ValueError('forecast for city requested not found')


@click.command()
@click.option('--city', prompt='choose city', help='Choose city for forecast')
@click.option('--forecast', default='TODAY', prompt='Choose day for forecast ',
              help='forecast days. EXAMPLE: TODAY, or TODAY+3 representing a 4 day forecast\n'
                   'Note: requesting TODAY+9 is the max forecast abilities')
@click.option('-c', 'unit', flag_value='CELSIUS', default=True, help='Set units to Celsius')
@click.option('-f', 'unit', flag_value='FAHRENHEIT', help='Set units to Fahrenheit')
def main(city, forecast, unit):
    weather = get_weather_in_city(city, unit)
    validate_weather(weather)
    days = get_amount_of_days_requested_from_cli(forecast, weather)
    print_forecast(days, weather)


if __name__ == '__main__':
    main()

