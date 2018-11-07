"""
 Description: Write to file my current location weather and print weather from a list of cities
"""

import json
import requests
import yaml
# from pprint import pprint

CITY_LIST = ['paris', 'new york', 'sydney', 'tokyo', 'london', 'montreal', 'Munich', 'Berlin', 'Zurich', 'melbourne']
WEATHER_API_KEY = '794fa52c482584de13e29fa980b607df'
FILE_NAME = "my_weather.txt"


def get_request(url, params=None):
    try:
        return json.loads(requests.get(url, params=params).content)
    except Exception:
        raise IOError("Error: Internet connection issues.")


def weather_to_file(wether, file):
    with open(file, "w") as f:
        yaml.dump(wether, f, default_flow_style=False, allow_unicode=True)


def get_my_city():
    response = get_request("http://ip-api.com/json")
    return response["city"]


def get_weather(city):
    payload = {'q': city, 'appid': WEATHER_API_KEY, "units": "metric"}
    weather = get_request("http://api.openweathermap.org/data/2.5/weather", payload)
    return weather


def get_country_by_code(code):
    return get_request("https://restcountries.eu/rest/v2/alpha/{0}".format(code))["name"]


def get_city_name(weather):
    return weather['name']


def get_temp(weather):
    return weather["main"]["temp"]


def get_country_code(weather):
    return weather["sys"]["country"]


def weather_print(city_list):
    for city in city_list:
        weather = get_weather(city)
        country = get_country_by_code(get_country_code(weather))

        print("The weather in {0}, {1} is {2} degrees.".format(get_city_name(weather), country, get_temp(weather)))


def main():
    my_city = get_my_city()
    my_weather = get_weather(my_city)
    weather_to_file(my_weather, FILE_NAME)
    weather_print(CITY_LIST)


if __name__ == '__main__':
    main()
