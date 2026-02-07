"""
Módulo para listar todos los documentos de una colección de MongoDB
"""


def list_all(mongo_collection):
    """
    Lista todos los documentos en una colección
    """
    return list(mongo_collection.find())
