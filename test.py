import requests
res = requests.post('http://192.168.1.5:8000/login', json={"name":"name","email":"lulalula","password":"123"})
if res.ok:
    print(res.json())