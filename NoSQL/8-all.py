#!/usr/bin/env pytho3
""" lists all documents"""

import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents"""
    return mongo_collection.find()
