class UserInterface:
        def __init__(self, weather_data_fetcher, data_parser):
            self.weather_data_fetcher = weather_data_fetcher
            self.data_parser = data_parser

        def display_weather(self, city):
            data = self.weather_data_fetcher.fetch_weather_data(city)
            if not data:
                print("Weather data not available")
            else:
                weather_report = self.data_parser.parse_weather_data(data)
                print(weather_report)

        def get_detailed_forecast(self, city):
            data = self.weather_data_fetcher.fetch_weather_data(city)
            return self.data_parser.parse_weather_data(data)
        
        def run(self):
            while True:
                city = input("Enter the city to get the weather forecast: ")
                if city.lower() == "exit":
                    print("Goodbye!")
                    break
                detailed = input("Would you like a detailed forecast? (yes/no): ").lower()
                if detailed == "yes":
                    forecast = self.get_detailed_forecast(city)
                else:
                    forecast = self.display_weather(city)
                print(forecast)