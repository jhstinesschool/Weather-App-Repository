#Hunter Stines Test Project Due Week 9
#Weather app that uses the OpenWeatherMap API to get weather data
import requests

#Function to get weather data from OpenWeatherMap API
def get_weather_data(location):
    api_key = "c984139344e7c994521c9d005472d7b2"
    # Tries to get weather data from OpenWeatherMap API and throws an exception if the request fails
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("\nSYSTEM: There was an error establishing a connection and getting weather data from OpenWeatherMap for the previous input please try again.\n")
        return None
    # If the request is successful, the data is returned as a JSON object
    data = response.json()
    return data

def main():
    location = ""
    # Asks the user for a location and queries the OpenWeatherMap API for the weather data using the requests module
    while(location != "0"):
        location = input("Enter city name or zip code (Enter 0 to exit program): ")
        if(location == "0"):
            break
        data = get_weather_data(location)
        if (data is None):
            continue
        # Prints the weather data to the console in a readable format
        print("\nSYSTEM: Weather data retrieved successfully\n")
        print("The weather forecast in {} is {}.".format(data["name"], data["weather"][0]["description"]))
        print("Temperature: {} Fahrenheit".format(data["main"]["temp"]))
        print("Humidity: {}".format(data["main"]["humidity"]))
        print("Wind Speed: {}".format(data["wind"]["speed"]))
        print()

if __name__ == '__main__':
    main()