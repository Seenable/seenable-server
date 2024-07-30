from app.feature.face_recognition_summary import FaceRecognitionSummary
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import app.feature.db as db
import base64
import numpy as np
import cv2
import uuid

app = FastAPI()

class Person(BaseModel):
    name: str
    image: UploadFile = File(...)

@app.post("/")
async def read_root(image: UploadFile = File(...)):
    contents = await image.read()

    jpeg = np.frombuffer(contents, dtype=np.uint8)
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
async def register_person(name: str = Form(...), image: UploadFile = File(...)):
    contents = await image.read()

    print(name)

    jpeg = np.frombuffer(contents, dtype=np.uint8)
    img = cv2.imdecode(jpeg, cv2.IMREAD_COLOR)
    uuid_id = str(uuid.uuid4())
    cv2.imwrite("./app/images/train/" + uuid_id + ".jpg",img)

    mongo = db.DB('seenable' , 'students')
    flag = mongo.insert_one({"_id": uuid_id,"name": name})
    return {"status": "OK", "name": name}

@app.get("/", response_class=HTMLResponse)
def show_register_view():
    return """
        <h1>hello world</h1>
    """

