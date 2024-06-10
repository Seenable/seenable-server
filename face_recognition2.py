import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import glob
import os
import db


known_face_encodings = []
known_face_names = []
files = glob.glob("./images/train/*")

for file in files:
    # print(file)
    # 画像を読み込み、顔の特徴値を取得する
    train_image = face_recognition.load_image_file(file)
    train_face_location = face_recognition.face_locations(train_image, model="hog")
    known_face_encodings.append(face_recognition.face_encodings(train_image, train_face_location)[0])
    known_face_names.append(os.path.split(file)[1].split('.')[0])
    # print(os.path.split(file)[1].split('.')[0])

# 画像を読み込み、顔の特徴値を取得する
test_img = face_recognition.load_image_file("images/test/IMG_2323.jpg")
test_img_location = face_recognition.face_locations(test_img, model="hog")
test_img_encoding = face_recognition.face_encodings(test_img, test_img_location)[0]

matches = face_recognition.compare_faces(known_face_encodings, test_img_encoding)
id = 0
face_distances = face_recognition.face_distance(known_face_encodings, test_img_encoding)
best_match_index = np.argmin(face_distances)
if matches[best_match_index]:
    id = known_face_names[best_match_index]

# 顔認証の結果を出力する

mongo = db.DB('seenable' , 'students')
find = mongo.find(filter={'_id': int(id)})

for doc in find:
    print(doc['name'])