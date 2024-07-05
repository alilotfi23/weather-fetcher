# Weather Information CLI

This project is a command-line interface (CLI) tool that fetches and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Retrieve current weather information for any city.
- Display weather conditions, description, temperature, and humidity.

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alilotfi23/weather-fetcher.git
   cd weather-fetcher
   ```

2. Install the required Python packages:
   ```bash
   pip install requests
   ```

## Usage

1. Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

2. Run the script with the city name and your API key:
   ```bash
   python weather.py London --api-key=YOUR_API_KEY
   ```

## Example

```bash
python weather.py London --api-key=14991fca5a1cf13e6a4719ab8660c154
```

Expected output:
```
Weather information:
Weather: Clear
Description: clear sky
Temperature: 289.92 K
Humidity: 68 %
```

## Code Overview

- `get_weather(city, api_key)`: Fetches weather data for the specified city using the provided API key.
- `main()`: Parses command-line arguments and displays the weather information.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

---

Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key.
