index_page =  \
"""
<link rel="stylesheet" type="text/css" href="/static/skins/sunburst.css">
<link rel="stylesheet" type="text/css" href="/static/prettify.css">
<script src="/static/prettify.js"></script>
<span>Thanks for checking this generator out!<span/>

<span>Below is some sample code behind the app that is running!</span>

<body onload="PR.prettyPrint()">
<pre class="prettyprint">
from flask import render_template
from flask_restful import Api
import ramp_routes as rroutes

app = Flask(__name__, static_url_path='/static')
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

    if __name__ == '__main__':
    # Change debug to False when in production
    # Add host='0.0.0.0' to test externally with ip address and not locally via localhost/127.0.0.0.1
    # Add port='9999' to change default port of 5000 to something else
    app.run(debug=True)
</pre>
<body>
"""

createYourOwn = \
"""
<link rel="stylesheet" type="text/css" href="/static/skins/sunburst.css">
<link rel="stylesheet" type="text/css" href="/static/prettify.css">
<script src="/static/prettify.js"></script>
<span>Route does not exist yet but its easy! Take a look at the example below!</span>
<body onload="PR.prettyPrint()">
<pre class="prettyprint">
# this goes into ramp_routes.py
class {{route}}(Resource):

    def get(self):
        return {"route":"{{route}}"}

# plug this into app.py before the if main clause
api.add_resource(rroutes.{{route}}, '/{{route}}')
</pre>
<span>Pretty easy huh?</span>
</body>
"""

class FlaskStuff:

    def __init__(self):
        pass

    header = """from flask import Flask, request
from flask import render_template
from flask_restful import Api
import ramp_routes as rroutes

app = Flask(__name__, static_url_path='/static')
api = Api(app)
"""

    index_func = """
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<route_name>')
def universal(route_name):
    return render_template('create.html', route=route_name)
"""
    route = """
class %s(Resource):

    def get(self):
        return {"route":"%s"}
"""

    resource = """
api.add_resource(rroutes.%s, '/%s')
"""


    rr_import = """from flask_restful import Resource
"""

    if_main = """
if __name__ == '__main__':
# Change debug to False when in production
# Add host='0.0.0.0' to test externally with ip address and not locally via localhost/127.0.0.0.1
# Add port='9999' to change default port of 5000 to something else
    app.run(debug=True)"""
