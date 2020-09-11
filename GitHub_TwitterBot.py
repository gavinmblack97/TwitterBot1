### Import all packages ###

import random
import requests
import tweepy
from pyzipcode import ZipCodeDatabase

### API for weather service ###

api_key = "API_KEY_FOR_OPEN_WEATHER"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

### START TWEET PROCESS ####

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API", "API_Secret")
auth.set_access_token("Access_Token", "Access_Token_Secret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

### SELECT ZIP CODE ###

zip_list = [17316, 10009, 17364, 77003, 35403, 27601, 28443, 20811, 59103, 80303, 94105, 53705, 20013, 23225, 15208,
            38107, 89124, 98118]

### Loop to check for valid zipcode. If zipcode is invalid it keeps trying

Keepgoing = True
while Keepgoing:

    try:
        A = random.choice(zip_list)
        zcdb = ZipCodeDatabase()
        zipcode = zcdb[A]

        Keepgoing = False

    except IndexError:
        print('Invalid ZIPCODE: ' + str(A))

### Print Location ###    

print("Selected Location: " + zipcode.city + '.' + zipcode.state)
print(' ')

### Get Weather Information using weather API ###

complete_url = base_url + "appid=" + api_key + "&zip=" + str(A)

response = requests.get(complete_url)

x = response.json()

y = x['main']

current_temp = y['temp']
temp_F = ((((current_temp - 273.15) / 5) * 9) + 32)

current_humidity = y['humidity']

z = x['weather']

current_description = z[0]['description']

### Create text for Tweet ###

tweet = "It is " + str(round(temp_F, 3)) + " °F" + " in " + zipcode.city + ', ' + zipcode.state

if (temp_F > 70):
    api.update_status(tweet + "\nNo, it is not Stout Weather")

else:
    api.update_status(tweet + "\nYes, it is Stout Weather")

