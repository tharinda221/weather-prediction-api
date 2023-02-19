from fastapi import FastAPI

# Import the get_weather_data function from the previous example
from get_weather_data import get_weather_data

# Create a new FastAPI app
app = FastAPI()

# Define an endpoint for getting the weather prediction for a given city
@app.get('/weather/{city_name}')
def get_weather(city_name: str):
    # Call the get_weather_data function to retrieve the weather prediction
    weather = get_weather_data(city_name)
    return weather
