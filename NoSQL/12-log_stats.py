#!/usr/bin/env python3
"""
Script que proporciona estadísticas sobre los logs de Nginx en MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Imprime estadísticas de la colección nginx en la base de datos logs.
    """
    # Conexión al cliente de MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Acceso a la base de datos 'logs' y la colección 'nginx'
    nginx_collection = client.logs.nginx

    # 1. Obtener el número total de documentos
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Mostrar conteo por métodos específicos
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Conteo de documentos con method=GET y path=/status
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
    
