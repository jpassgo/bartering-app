from django.conf import settings
from pymongo import MongoClient


def create_mongo_connection():
    return MongoClient(settings.MONGODB_URI)


def get_postings_table(client):
    db = client['postings_db']
    return db.postings


def insert_posting(user_id, posting):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    posting['user_id'] = user_id
    return postings_table.insert_one(posting)


def retrieve(id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    posting = postings_table.find_one({'id': id})
    posting['_id'] = str(posting.get('_id'))
    return posting


def retrieve_postings_for_user(user_id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    postings = postings_table.find({'user_id': user_id})
    return postings


def update_posting(id, updated_posting_attributes):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)

    query = {"id": id}
    new_values = {"$set": updated_posting_attributes}

    postings_table.update_one(query, new_values)


# Need to loop over the postings for a
def delete(id):
    client = create_mongo_connection()
    postings_table = get_postings_table(client)
    postings_table.delete_one({'id': id})

