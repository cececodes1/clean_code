from weather_data import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface

def main():
    weather_data_fetcher = WeatherDataFetcher()
    data_parser = DataParser()
    user_interface = UserInterface(weather_data_fetcher, data_parser)
    user_interface.run()

if __name__ == "__main__":
    main()