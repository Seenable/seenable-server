import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# 画像を読み込み、顔の特徴値を取得する
arata_image = face_recognition.load_image_file("images/train/train_img1.png")
arata_face_location = face_recognition.face_locations(arata_image, model="hog")
arata_face_encoding = face_recognition.face_encodings(arata_image, arata_face_location)[0]

shirota_image = face_recognition.load_image_file("images/train/train_img2.png")
shirota_face_location = face_recognition.face_locations(shirota_image, model="hog")
shirota_face_encoding = face_recognition.face_encodings(shirota_image, shirota_face_location)[0]

known_face_encodings = [
    arata_face_encoding,
    shirota_face_encoding,
]
known_face_names = [
    "新田真剣佑",
    "城田優",
]

# 画像を読み込み、顔の特徴値を取得する
test_img = face_recognition.load_image_file("images/test/test_img2.png")
test_img_location = face_recognition.face_locations(test_img, model="hog")
test_img_encoding = face_recognition.face_encodings(test_img, test_img_location)[0]

matches = face_recognition.compare_faces(known_face_encodings, test_img_encoding)
name = "Unknown"
face_distances = face_recognition.face_distance(known_face_encodings, test_img_encoding)
best_match_index = np.argmin(face_distances)
if matches[best_match_index]:
    name = known_face_names[best_match_index]

# 顔認証の結果を出力する
print(name)