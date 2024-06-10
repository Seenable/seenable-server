import db
import face_recognition_summary

face_recognition_summary = face_recognition_summary.FaceRecognitionSummary()
id = face_recognition_summary.match_face("IMG_2323.jpg")
mongo = db.DB('seenable' , 'students')
find = mongo.find(filter={'_id': int(id)})

for doc in find:
    print(doc['name'])