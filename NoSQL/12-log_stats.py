#!/usr/bin/env python3
"""
Módulo que proporciona estadísticas sobre los logs de Nginx almacenados en MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Muestra estadísticas sobre la colección nginx en la base de datos logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Conteo total de logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Estadísticas por métodos
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Conteo de status check (GET a /status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
