from django.conf import settings
from pymongo import MongoClient

if not settings.MONGO_URI:
    raise RuntimeError(
        "falta configurar MONGO_URI en el archivo .env"
    )

cliente = MongoClient(  
    settings.MONGO_URI,
    serverSelectionTimeoutMS=500
)

db = cliente[settings.MONGO_DB]
coleccion_productos = db["productos"]