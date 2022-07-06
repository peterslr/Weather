#This program uses the weather api to get historical forecast info for a city and date input by the user
#version 2.2 July 6,2022
import requests
import json
import pprint
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine

#create a dataframe to hold the api data
col_names=['City', 'Country', 'Date', 'Latitude', 'Longitude']
df=pd.DataFrame(columns=col_names)

#Get the users input
userscity=input("What city would you like weather data for?")
usersdate=input("What recent date would you like weather data for? Please use format yyyy-MM-dd")

#Define info needed for the API call
url = "https://weatherapi-com.p.rapidapi.com/history.json"
querystring = {"q":userscity,"dt":usersdate,"lang":"en"}
headers = {
	"X-RapidAPI-Key": "f7371d9043msh860d65fe42a3affp10bab1jsnb8c63d7a9318",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

#Convert the api data to a Python dictionary
response = requests.request("GET", url, headers=headers, params=querystring)
dict_data=json.loads(response.text)
pprint.pprint(dict_data)

#Filter the dictionary data to move selected information into the dataframe
df.loc[len(df.index)] = [userscity, dict_data['location']['country'], usersdate, dict_data['location']['lat'], dict_data['location']['lon']]
print(df)

#Create database and move the dataframe into a database
engine=db.create_engine('sqlite:///weatherdatabase.db')
df.to_sql('basic_info', con=engine, if_exists='replace', index=False)

#Query the database and print the result
query_result=engine.execute("select City, Longitude from basic_info;").fetchall()
print(pd.DataFrame(query_result))