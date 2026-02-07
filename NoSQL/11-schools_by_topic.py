#!/usr/bin/env python3
"""
Módulo para filtrar documentos en una colección de MongoDB por tema.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Devuelve una lista de escuelas que tienen un tema específico.

    Args:
        mongo_collection: Objeto de colección de pymongo.
        topic (str): El tema buscado en la lista de temas de la escuela.

    Returns:
        Una lista de documentos que coinciden con el tema buscado.
    """
    return list(mongo_collection.find({"topics": topic}))
