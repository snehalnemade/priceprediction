import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'area':2000, 'bedroom':2, 'age':6})

print(r.json())