from fastapi import FastAPI, HTTPException
from bson.objectid import ObjectId

app = FastAPI()

@app.post("/api/eventos")
def agregar_evento(evento: Evento):
    nuevo_evento = evento.dict()


    resultado = eventos_collection.insert_one(nuevo_evento)


    nuevo_evento["_id"] = str(resultado.inserted_id)

    return {
        "mensaje": "Evento creado exitosamente",
        "evento": nuevo_evento
    }
