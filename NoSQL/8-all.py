#!/usr/bin/env pytho3
""" lists all documents"""


import pymongo


def list_all(mongo_collection):
    """ lists all documents"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
