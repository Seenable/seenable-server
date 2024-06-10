from app.feature.face_recognition_summary import FaceRecognitionSummary
from fastapi import FastAPI
import app.feature.db as db

app = FastAPI()

@app.get("/")
def read_root():
    # return {"Hello": "World"}
    face_recognition_summary = FaceRecognitionSummary()
    id = face_recognition_summary.match_face("IMG_2323.jpg")
    mongo = db.DB('seenable' , 'students')
    find = mongo.find(filter={'_id': int(id)})
    name = "no"
    for doc in find:
        print(doc['name'])
        name = doc['name']
    return { "name" : name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

