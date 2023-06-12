import requests
from dotenv import load_dotenv 
import pandas as pd 
import json 
import os

api_key=os.getenv('API_KEY')
# print(api_key)
# https://api.openweathermap.org/data/2.5/weather?q=Jacksonville&appid=e013c742a8a2882abe22def544e5e770
try:
    response=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Jacksonville&appid=e013c742a8a2882abe22def544e5e770")
    if response.status_code==200:
        data = response.json()
        print(data)
    else:
        print(f"Request failed. Failure code:",response.status_code)
except requests.exceptions.RequestException as a:
    print('Please debug your request. Error response', a)



