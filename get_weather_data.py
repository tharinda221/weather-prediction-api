import requests

# Replace YOUR_API_KEY with your OpenWeatherMap API key
api_key = '62994fe039b23d9c6aaa996ee152801d'

# Define the base URL for the OpenWeatherMap API
base_url = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name):
    """Retrieves the current weather data for a city from the OpenWeatherMap API."""
    # Define the query parameters for the API request
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

    # Send the API request and retrieve the response
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the relevant weather data62994fe039b23d9c6aaa996ee152801d
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
        return weather
    else:
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

# Example usage: get the current weather data for New York City
# weather = get_weather_data('New York City')
# print(weather)