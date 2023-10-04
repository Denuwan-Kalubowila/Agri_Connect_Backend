from pymongo import MongoClient

client=MongoClient("mongodb+srv://Vishwa:54321@cluster0.1ovqgie.mongodb.net/?retryWrites=true&w=majority")

db=client.agri_connect
collection=db["user"]