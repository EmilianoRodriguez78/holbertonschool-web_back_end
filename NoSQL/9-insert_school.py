#!/usr/bin/env python3
"""
Módulo para insertar un documento en una colección de MongoDB.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserta un nuevo documento en una colección basado en kwargs.

    Args:
        mongo_collection: Objeto de colección de pymongo.
        **kwargs: Atributos del documento a insertar.

    Returns:
        El _id del nuevo documento insertado.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
  
