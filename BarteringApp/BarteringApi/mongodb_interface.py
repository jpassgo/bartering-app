from django.conf import settings
from pymongo import MongoClient


def create_mongo_connection():
    return MongoClient(settings.MONGODB_URI)


def get_postings_table(client):
    db = client['postings_db']
    return db.postings


def create(posting):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    return postings_table.insert_one(posting).inserted_id


def retrieve(id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    posting = postings_table.find_one({'id': id})
    posting['_id'] = str(posting.get('_id'))
    return posting


def retrieve_postings_for_user(user_id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    posting = postings_table.find_one({'user_id': user_id})
    posting['user_id'] = str(posting.get('user_id'))
    return posting


def update(id, updated_posting_attributes):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)

    query = {"id": id}
    new_values = {"$set": updated_posting_attributes}

    postings_table.update_one(query, new_values)


def delete(id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    postings_table.delete_one({'id': id})
