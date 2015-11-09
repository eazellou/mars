
from flask import *
import requests

app = Flask(__name__)

main = Blueprint('main', __name__, template_folder='views')


@main.route('/')
def main_route():

    #AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M is API key for google geolocation
    #https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M
    #administrative_area_level_3

    latlongRaw = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M", data={})
    latlong = latlongRaw.json()

    location_request = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latlong['location']['lat']) + "," + str(latlong['location']['lng']) + "&result_type=administrative_area_level_2&key=AIzaSyDLkw1t2_XtyMMVb4iGdKBmnC0xNiVX25M"
    
    locationRaw = requests.get(location_request)
    locationJSON = locationRaw.json()
    
    location = locationJSON['results'][0]['formatted_address']
    sep = ','
    location = location.split(sep, 1)[0]





    marsRaw = requests.get('http://marsweather.ingenology.com/v1/latest/')
    mars = marsRaw.json()
    print '_________MARS__________'
    print mars['report']
    return render_template("mars.html", mars=mars['report'], location = location)