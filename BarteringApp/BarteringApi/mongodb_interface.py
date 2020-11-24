from rest_framework.parsers import JSONParser
from django.conf import settings
from pymongo import MongoClient


def create_mongo_connection():
    return MongoClient(settings.MONGODB_URI)

def insert(posting):
    mongo_connection = create_mongo_connection()

def retrieve(id):
    pass

def update(id, updated_post_attributes):
    pass

def delete(id):
    pass