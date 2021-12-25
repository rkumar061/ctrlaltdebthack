import requests
res = requests.post('http://139.59.77.191:8000/login', json={"email":"email","password":"password@user"})
if res.ok:
    print(res.json())