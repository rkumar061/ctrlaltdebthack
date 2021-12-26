import requests
res = requests.post('http://139.59.77.191:8000/data/create', json={"role": "s","name": "name","email":"lud","password":"123"})
if res.ok:
    print(res.json())