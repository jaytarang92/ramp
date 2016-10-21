from flask import Flask, request
from flask import render_template
from flask_restful import Api
import ramp_routes as rroutes

app = Flask(__name__, static_url_path='/static')
api = Api(app)



@app.route('/')
def index():
    return render_template('index.html')


api.add_resource(rroutes.crap, '/crap')

if __name__ == '__main__':
    # Change debug to False when in production
    # Add host='0.0.0.0' to test externally with ip address and not locally via localhost/127.0.0.0.1
    # Add port='9999' to change default port of 5000 to something else
    app.run(debug=True)
