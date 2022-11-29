from bs4 import BeautifulSoup
import requests

print("Let's check the weather:")
city = input("What city's weather would you like to check? ")
state = input("What state is that in?")

url = f"https://www.wunderground.com/weather/us{state}/{city}"

response = requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')

temp = soup.find(class_='wu-value wu-value-to')
int_temp = int(temp.text)

comfortability = ''

if int_temp >= 90:
    comfortability = "too hot!!!"
elif int_temp < 90 and int_temp >=65:
    comfortability = "just right!"
else:
    comfortability = "it's too freaking cold!!!"

print(f'The current temp is {int_temp}. It\'s {comfortability}')