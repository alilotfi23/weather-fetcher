import requests
import argparse

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument("city", type=str, help="City name")
    parser.add_argument("--api-key", required=True, type=str, help="Your OpenWeatherMap API key")

    args = parser.parse_args()

    weather_data = get_weather(args.city, args.api_key)

    if weather_data:
        print("Weather information:")
        print(f"Weather: {weather_data['weather'][0]['main']}")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']} K")
        print(f"Humidity: {weather_data['main']['humidity']} %")
    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    main()

'''
python weather.py London --api-key=14991fca5a1cf13e6a4719ab8660c154

'''
