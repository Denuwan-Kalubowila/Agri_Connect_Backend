from pymongo import MongoClient

client=MongoClient("mongo uri")

db=client.agri_connect
collection=db["user"]