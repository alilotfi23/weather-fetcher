import requests  # Import the requests library to make HTTP requests
import argparse  # Import argparse to handle command-line arguments

def get_weather(city, api_key):
    """
    Fetch the weather data for a specified city using OpenWeatherMap API.

    Args:
        city (str): The name of the city for which to retrieve weather data.
        api_key (str): Your OpenWeatherMap API key for authentication.

    Returns:
        dict or None: Returns weather data as a dictionary if successful, otherwise None.
    """
    # Construct the API request URL with the city name and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the data
        data = response.json()
        return data
    else:
        # Return None if the request failed
        return None

def main():
    """
    Main function to execute the script. It parses command-line arguments,
    retrieves weather data, and prints it in a readable format.
    """
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    
    # Add a positional argument for the city name
    parser.add_argument("city", type=str, help="City name")
    
    # Add an optional argument for the API key (required)
    parser.add_argument("--api-key", required=True, type=str, help="Your OpenWeatherMap API key")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the get_weather function with the provided city and API key
    weather_data = get_weather(args.city, args.api_key
