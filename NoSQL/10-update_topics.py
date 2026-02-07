#!/usr/bin/env python3
"""
Módulo para actualizar documentos en una colección de MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Cambia todos los temas de un documento de la escuela basado en el nombre.

    Args:
        mongo_collection: Objeto de colección de pymongo.
        name (str): El nombre de la escuela a actualizar.
        topics (list of str): Lista de temas abordados en la escuela.

    Returns:
        Nada.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
  
