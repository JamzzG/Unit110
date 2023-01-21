import pymongo
import certifi  

connection_str = "mongodb+srv://JamesDB:Test123@cluster0.z59nvld.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where() )
db = client.get_database("OnlineStore")