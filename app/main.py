from app.feature.face_recognition_summary import FaceRecognitionSummary
from fastapi import FastAPI
from pydantic import BaseModel
import app.feature.db as db
import base64
import numpy as np
import cv2
import uuid

app = FastAPI()

class Image(BaseModel):
    image: bytes

class Person(BaseModel):
    name: str
    image: bytes

@app.post("/")
def read_root(image: Image):
    decodeImg = base64.b64decode(image.image)

    jpeg = np.frombuffer(decodeImg, dtype=np.uint8)
    img = cv2.imdecode(jpeg, cv2.IMREAD_COLOR)

    face_recognition_summary = FaceRecognitionSummary()
    id = face_recognition_summary.match_face(img)
    mongo = db.DB('seenable' , 'students')
    find = mongo.find(filter={'_id': str(id)})
    name = "no"
    for doc in find:
        name = doc['name']
    return { "name" : name}

@app.post("/person")
def register_person(person: Person):
    print(person.name)
    decodeImg = base64.b64decode(person.image)

    jpeg = np.frombuffer(decodeImg, dtype=np.uint8)
    img = cv2.imdecode(jpeg, cv2.IMREAD_COLOR)
    uuid_id = str(uuid.uuid4())
    cv2.imwrite("./app/images/train/" + uuid_id + ".jpg",img)

    mongo = db.DB('seenable' , 'students')
    flag = mongo.insert_one({"_id": uuid_id,"name": person.name})
    return "aa"

