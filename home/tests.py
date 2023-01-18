import requests
r=requests.get('http://127.0.0.1:8000/todos/?user=admin')
print(r.content)