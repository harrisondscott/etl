import mysql.connector
import requests
from pymongo import MongoClient
import json

def getWeather(zipCode):
    request = str("http://api.weatherapi.com/v1/current.json?key=32043143427e4d3d83e34557211001&q=") + zipCode
    return requests.get(request).text
    

client = MongoClient('localhost', 27017)
db = client['weather_db']
collection = db['current']

myConnector = mysql.connector.connect(user='harrison', password='8hY&BZZaa@#!', host='127.0.0.1', database='weather', auth_plugin='mysql_native_password')
mycursor = myConnector.cursor()

mycursor.execute("SELECT * FROM user_info")

myresult = mycursor.fetchall()

for x in myresult:
    _, _, _, zipCode = x
    collection.insert(json.loads(getWeather(zipCode)))
