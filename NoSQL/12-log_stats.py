#!/usr/bin/env python3
"""script that provides some stats about Nginx logs"""

from pymongo import MongoClient


if __name__ == "__main__":
    """script that provides some stats about Nginx logs"""
    client = MongoClient()
    db = client.logs.nginx
    doc_count = db.estimated_document_count()
    print("{} logs".format(doc_count))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = db.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    status_count = db.count_documents(
        {
            "method": "GET",
            "path": "/status",
        }
    )

    print("{} status check".format(status_count))
