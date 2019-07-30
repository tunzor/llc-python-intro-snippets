# This is an example of using an API to get data from another system
# Read more about APIs here - https://zapier.com/learn/apis/chapter-1-introduction-to-apis/

# A large collection of free APIs are available for perusal here
# https://github.com/public-apis/public-apis

# This example uses a free weather API hosted by MetaWeather - https://www.metaweather.com

# Import requests library; this allows us to make a call to get a webpage
import requests

# Our city variable
city = 'toronto'
print("Weather for", city)
print("--------------------------")

# The block of code below looks up the location code used by the
# Metaweather API and saves it into the variable cityId

# Endpoints are URLs that we can make calls against to get data from a system
# This endpoint allows us to enter a city and returns the city id
locationEndpoint = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)

# Here we make the call to the API (requests.get(locationEndpoint)),
# save the response data (which comes back in JSON form),
# and use it to extract and save the city id (note: woeid is defined by MetaWeather, not us)
locationData = requests.get(locationEndpoint).json()[0]
cityId = locationData["woeid"]

# Another API call to look up the weather data for the city we looked
# up with the previous API call
weatherEndpoint = 'https://www.metaweather.com/api/location/{}'.format(cityId)
weatherData = requests.get(weatherEndpoint).json()

# The API call above returns 5 days of weather: today and the next four days
# Here we loop over each date returned from the API, print it, the temperature
# (formatting to 2 decimal places), and the current weather condition
for date in weatherData['consolidated_weather']:
    print(date['applicable_date'], ":", "{:.2f}".format(date['the_temp']), "degrees and", date['weather_state_name'])
