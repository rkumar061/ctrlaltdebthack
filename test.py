import requests
res = requests.post('http://192.168.1.5:8000/data/create', json={"name": "name","email":"lud","password":"123"})
if res.ok:
    print(res.json())