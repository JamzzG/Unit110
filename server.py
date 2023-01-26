from flask import Flask, request
from flask import jsonify
# need to be sure to add the ,request above
import json
from mock_data import catalog
from config import db
from flask_cors import CORS

app = Flask ("server")
CORS(app) # disable CORS to allow requests from any origin

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
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"]) #fixes the _id issue with db
        results.append(prod)
    return json.dumps(results)


#save products
@app.post("/api/catalog")
def save_catalog():
    product = request.get_json()
    db.products.insert_one(product)

    product["_id"] = str(product["_id"]) #clean the ObjectId ('asd') from the object
    
    print (product)
    return json.dumps(product)

# get all products that belong to a category
@app.get("/api/catalog/<category>")
def get_by_category(category):
    cursor = db.products.find ({"category": category})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"]) 
        results.append(prod)
    return json.dumps(results)


@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    cursor = db.products.find ({"title": {"$regex": title, "$options": "i"} }) #"$regex": title means not an exact match...but one that contains the string searched. and "$options": "i" means it is a case insensitive search.  result will show under api/category/search/string_searched
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"]) 
        results.append(prod)
    return json.dumps(results)

    
@app.get("/api/product/cheaper/<limit>")
def cheaper_than(limit):
    cursor = db.products.find ({}) 
    result = []
    for prod in cursor:
        if prod["price"]< float(limit):
            prod["_id"] = str(prod["_id"]) 
            result.append(prod)

    return json.dumps(result)

@app.get("/api/product/total_items")
def total_items():
    count = db.products.count_documents({})
    return jsonify(count)



# @app.route("/api/product/total_items")   ***This ia an older method.  The .route method allows more than get requests but using .get is still preferred in this case. ***
# def total_items():
#     count = db.products.count()
#     return json.dumps(count)







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
    cursor = db.products.find ({}) 
    answer = cursor [0]
    for prod in cursor:
        if prod["price"] < answer["price"]:
            
            answer = prod

    answer["_id"] = str(answer["_id"])
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
