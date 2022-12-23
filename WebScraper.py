import requests
from bs4 import BeautifulSoup

#taking input from user

city = str(input("Enter city name = "))

#creating url
url = "https://www.google.com/search?q=" + "weather" + city

html = requests.get(url).content

# getting the raw data
soup = BeautifulSoup(html, 'html.parser')

#getting the temperature
temp = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text

#getting time and sky description
time_skyDescription = soup.find('div', attrs = {'class': 'BNeawe tAd8D AP7Wnd'}).text

#formatting the data
data = time_skyDescription.split('\n')
time = data[0]
sky = data[1]

#list which is having all div tags with partuclar class names
listdiv = soup.findAll('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'})

#the data we need is available at index s
strd = listdiv[5].text

#formatting the string
pos = strd.find('Wind')
otherData = strd[pos:]

#printing the data
print("Temperature is: ", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(otherData)










