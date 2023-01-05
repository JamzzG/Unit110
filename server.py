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


@app.get("/api/catalog/<category>")
def get_by_category(category):
    result = []
    for prod in catalog:
        if prod["category".lower()] == category.lower():
            result.append(prod)

    return json.dumps(result)


@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    result = []
    for item in catalog:
        if title.lower() in item["title"].lower():
            result.append(item)
    
    return json.dumps(result)
    
@app.get("/api/product/cheaper/<limit>")
def cheaper_than(limit):
    result = []
    for prod in catalog:
        if prod["price"]< float(limit):
            result.append(prod)

    return json.dumps(result)


@app.get("/api/product/total_items")
def total_items():
    count = len(catalog)
    return json.dumps(count)
#     json.dumps 


# The code below was modified from CHAT GPT
@app.get("/api/product/lowest")
def find_lowest_price():
    lowest_price = float('inf')
    lowest_priced_item = None
    for item in catalog:
        if item['price'] < lowest_price:
            lowest_priced_item = item
            lowest_price = item['price']
    return json.dumps(lowest_priced_item)
    
@app.get("/api/product/cheapest")
def get_cheapest():
    answer = catalog [0]
    for prod in catalog:
        if prod["price"] < answer["price"]:
            answer = prod 
    return json.dumps(answer)







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
