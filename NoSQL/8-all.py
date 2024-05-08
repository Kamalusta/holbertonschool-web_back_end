#!/usr/bin/env python3
""" lists all documents"""
import pymongo


def list_all(mongo_collection):
    """List doc function"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
