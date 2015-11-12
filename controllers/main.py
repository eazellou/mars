from flask import *
import requests
import math

app = Flask(__name__)

main = Blueprint('main', __name__, template_folder='views')

def kelvinToFahrenheit(kelvin):
    return (kelvin - 273.15)* 1.8000 + 32.00


@main.route('/')
def main_route():

    #AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M is API key for google geolocation
    #https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M
    #administrative_area_level_2
    #d307b45f9ddbd64a8b6ebc51767f1d01 is appid for weather report

    latlongRaw = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M", data={})
    latlong = latlongRaw.json()

    lat = str(latlong['location']['lat'])
    lng = str(latlong['location']['lng'])

    location_request = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + lng + "&result_type=administrative_area_level_2&key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M"
    
    locationRaw = requests.get(location_request)
    locationJSON = locationRaw.json()
    
    location = locationJSON['results'][0]['formatted_address']
    sep = ','
    location = location.split(sep, 1)[0]

    #local weather
    weather_request = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lng + "&appid=d307b45f9ddbd64a8b6ebc51767f1d01"

    weatherRaw = requests.get(weather_request)
    weather = weatherRaw.json()

    #convert pressure to atm
    localatm = weather['main']['grnd_level'] / 1013.25
    localatm = round(localatm, 2)
    weather['main']['grnd_level'] = localatm
    print '____________WEATHER______________'
    print weather['weather'][0]['main']

    #convert temperatures to Fahrenheit
    weather['main']['temp'] = round(kelvinToFahrenheit(weather['main']['temp']), 2)



    print '__________LOCAL_________'
    print weather



    marsRaw = requests.get('http://marsweather.ingenology.com/v1/latest/')
    mars = marsRaw.json()
    marsatm = mars['report']['pressure'] / 1013.25
    marsatm = round(marsatm, 2)
    mars['report']['pressure'] = marsatm
    print '_________MARS__________'
    print mars['report']


    return render_template("mars.html", mars=mars['report'], local = weather, location = location)




