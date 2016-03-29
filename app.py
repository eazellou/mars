
from flask import Flask, render_template
import controllers


app = Flask(__name__, template_folder='views')

app.register_blueprint(controllers.main)

app.secret_key = '0#q!oj#*!ipb&^$p$$dsn-v06^q&$as76k*1(v5x4w&hagb+_4'

# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(debug=True)
