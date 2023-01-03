from flask import Flask
import json
from mock_data import catalog

app = Flask ("server")

@app.get ("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this another endpoint named test"

    return "James Grantham <br> granthamjames@email.com"

# debug needs to be True for development and False at Prodcution
####################################################
#####################CATALOG API #####################
#####################################################

@app.get ("/api/version")
def version():
    version = {
        "V" : "V.1.0.1",
        "name": "Rubber_Ducky_Firewall",
        "yourzip": "87105",
    }
    return json.dumps (version)


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

@app.get("/test/numbers")
def get_numbers():
    # create a list with numbers from 1 to 20
    # except 13 and 17
    # and return the list as json
    res = []
    for n in range(1, 21):
        if n  != 13 and n!= 17:
            res.append(n)

    return json.dumps (res)



app.run (debug=True) 
