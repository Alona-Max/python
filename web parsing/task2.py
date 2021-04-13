import requests
# pip install requests
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q=vancouver&appid=6927ae0be1d5362bbefb937e3e7a59eb"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.114 Safari/537.36"
}
response = requests.get(url)
print(response)
pprint(response.text)
