import requests
from bs4 import BeautifulSoup

# Enter your city's name below
city = "rajahmundry"

# Fetch the HTML content of the weather page for your city
url = f"https://www.google.com/search?q={city}+weather"
html = requests.get(url).content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Get the temperature, location and time of the weather
temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
location = soup.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text

# Print the weather information
print(temperature,'\n',location)
