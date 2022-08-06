import json 
import requests


url = 'http://127.0.0.1:8000/recommend'
input_data = {
    "place_name": "Phewa Lake"
}

input_json = json.dumps(input_data)
response = requests.post(url, data=input_json)
print(response.text)