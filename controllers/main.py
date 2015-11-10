
from flask import *
import requests

app = Flask(__name__)

main = Blueprint('main', __name__, template_folder='views')


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


    weather_request = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lng + "&appid=d307b45f9ddbd64a8b6ebc51767f1d01"

    weatherRaw = requests.get(weather_request)
    weather = weatherRaw.json()
    print '__________LOCAL_________'
    print weather



    marsRaw = requests.get('http://marsweather.ingenology.com/v1/latest/')
    mars = marsRaw.json()
    print '_________MARS__________'
    print mars['report']
    return render_template("mars.html", mars=mars['report'], location = location)