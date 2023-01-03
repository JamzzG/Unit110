from flask import Flask
import json

app = Flask ("server")

@app.get ("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this another endpoint named test"

@app.get ("/about")
def about():
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







app.run (debug=True) 
