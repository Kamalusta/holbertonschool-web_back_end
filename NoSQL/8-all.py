#!/usr/bin/env pytho3
""" lists all documents"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents"""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
