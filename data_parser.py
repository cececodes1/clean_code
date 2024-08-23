class DataParser:
        def parse_weather_data(self, data):
            if not data:
                return "Weather data not available"
            city = data["city"]
            temperature = data["temperature"]
            condition = data["condition"]
            humidity = data["humidity"]
            return f"Weather in {city}: {temperature}°F, {condition}, Humidity: {humidity}%"