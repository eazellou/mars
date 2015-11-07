
from flask import *
import requests

app = Flask(__name__)

main = Blueprint('main', __name__, template_folder='views')


@main.route('/')
def main_route():

    marsRaw = requests.get('http://marsweather.ingenology.com/v1/latest/')
    mars = marsRaw.json()
    print mars['report']
    return render_template("mars.html", mars=mars['report'])