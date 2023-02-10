# A News API for news retrieval
import requests
import json

# prompt for entering a user's news API key
API_key = '8ed07e19843b4ea29b4bda8a0cf736c4'

topic = input('Please enter the news topic that you want: ')
num = input('Please enter the number (not exceeding 100) of news you want: ')
date = input('Please enter the start date in the form like \'2022-02-01\', then you will get news from this day: ')

url = ('http://newsapi.org/v2/everything?'
       'q='+topic+'&'
       'from='+date+'&'
       'sortBy=popularity&'
       'pageSize='+num+'&'
       'apiKey='+API_key)

response = requests.get(url)
output = json.dumps(response.json(), indent=4)
f = open(r'C:\Users\32179\Desktop\CityU\6941\Tutorial(Week4) 2\News.txt', 'w', encoding='utf-8')
for i in output:
    f.write(i)
f.close()