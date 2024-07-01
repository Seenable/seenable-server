from app.feature.face_recognition_summary import FaceRecognitionSummary
from fastapi import FastAPI
from pydantic import BaseModel
import app.feature.db as db
import base64
import numpy as np
import cv2

app = FastAPI()

class Image(BaseModel):
    image: bytes

@app.post("/")
def read_root(image: Image):
    decodeImg = base64.b64decode(image.image)

    jpeg = np.frombuffer(decodeImg, dtype=np.uint8)
    img = cv2.imdecode(jpeg, cv2.IMREAD_COLOR)

    face_recognition_summary = FaceRecognitionSummary()
    id = face_recognition_summary.match_face(img)
    mongo = db.DB('seenable' , 'students')
    find = mongo.find(filter={'_id': int(id)})
    name = "no"
    for doc in find:
        name = doc['name']
    return { "name" : name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
