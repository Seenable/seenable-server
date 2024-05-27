import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# 画像を読み込み、顔の特徴値を取得する
arata_image = face_recognition.load_image_file("images/train/train_img1.png")
arata_face_location = face_recognition.face_locations(arata_image, model="hog")
arata_face_encoding = face_recognition.face_encodings(arata_image, arata_face_location)[0]

known_face_encodings = [
    arata_face_encoding,
]
known_face_names = [
    "新田真剣佑",
]

# 画像を読み込み、顔の特徴値を取得する
test_img = face_recognition.load_image_file("images/test/test_img1.png")
test_img_location = face_recognition.face_locations(test_img, model="hog")
test_img_encoding = face_recognition.face_encodings(test_img, test_img_location)[0]

dists = face_recognition.face_distance(known_face_encodings, test_img_encoding)

answer = '人が違います'
for dist in dists:
    if dist < 0.45:
        answer = known_face_names[0]

# 顔認証の結果を出力する
print(answer)