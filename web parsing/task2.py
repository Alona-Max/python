import requests
# pip install requests
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q=vancouver&appid=6927ae0be1d5362bbefb937e3e7a59eb"
response = requests.get(url)
print(response)
pprint(response.text)
