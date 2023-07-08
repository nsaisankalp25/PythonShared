import pyowm
owm = pyowm.OWM('APIKEY')
weather_mgr = owm.weather_manager()
place = 'Hyderabad, IN'
observation = weather_mgr.weather_at_place(place)

temperature = observation.weather.temperature("celsius")["temp"]
humidity = observation.weather.humidity
wind = observation.weather.wind()
gust = observation.weather
print(dir(gust))
print(gust.pressure)
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')
print(f'Wind Speed: {wind["speed"]} m/s')
