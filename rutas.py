from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = FastAPI()

# Conexión a MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["agenda"]
eventos_collection = db["eventos"]

@app.get("/api/eventos")
def obtener_eventos(usuario_id: str = Query(..., description="ID del usuario")):
    eventos = list(eventos_collection.find({"usuario_id": usuario_id}).sort([("fecha", 1), ("hora", 1)]))
    
    for evento in eventos:
        evento["_id"] = str(evento["_id"])  # Convertimos ObjectId a string

    return eventos
