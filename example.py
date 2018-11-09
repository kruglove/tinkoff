import requests
response = requests.get('https://api.github.com/users/kruglove')
print(response.text)