import requests
myappid='e8dacbff'
url='https://trackapi.nutritionix.com/v2/natural/nutrients'
userinput=input("Type the food you want nutrition info for")
headers = {'Content-Type': 'application/json','x-app-id': myappid, 'x-app-key': '50ebf945b7878e85d272f6a69086bd2e'}
body={'query': userinput, 'timezone': 'US/Eastern'}
response=requests.post(url, body, headers=headers)
print(response.json())