import requests
import json

choice = int(input("enter 1 for cam and 2 for reg: 3 for noew vid"))
localhost = "http://localhost:8080/"
if choice is 1:
    payload = """{"user_name":"tom","location":"office"}"""
    localhost = "http://localhost:8080/addCamera"
elif choice is 2:
    payload = """{"user_name":"tom","location":"office"}"""
    localhost = "http://localhost:8080/addCamera"
else:
    payload = """{"user_name":"tom","password":"tom","method":"register"}"""
    localhost = "http://localhost:8080/user"

url = 'http://www.upbeat-element-358.appspot.com/'

headers = {'content-type': 'application/json'}

response = requests.post(url+"user", data=json.dumps(payload), headers=headers)
x = response.text
print(x)





