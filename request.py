import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':11.8,})
print(r.json())