import requests

apiKey = "8021ff66b91d5e667f6767a71a0dadbf"

city = "Dublin"
url = f"https://samples.openweathermap.org/data/2.5/find?q={city}&units=metric&appid={apiKey}"
r = requests.get(url)

weatherData = r.json()["list"][0]


output = f'''Weather for {city.capitalize()}:
Current temperature - {weatherData["main"]["temp"]} degrees celsius'''
print(output)

for i in weatherData["weather"]:
  print(f"- {i['main']}")