import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import glob
import os
import db

class FaceRecognitionSummary() :
    known_face_encodings = []
    known_face_names = []

    def __init__(self):
        files = glob.glob("./images/train/*")
        for file in files:
            print(file)
            # 画像を読み込み、顔の特徴値を取得する
            train_image = face_recognition.load_image_file(file)
            train_face_location = face_recognition.face_locations(train_image, model="hog")
            self.known_face_encodings.append(face_recognition.face_encodings(train_image, train_face_location)[0])
            self.known_face_names.append(os.path.split(file)[1].split('.')[0])

    def __receive_test_image(self, imgName):
        test_img = face_recognition.load_image_file("images/test/" + imgName)
        test_img_location = face_recognition.face_locations(test_img, model="hog")
        test_img_encoding = face_recognition.face_encodings(test_img, test_img_location)[0]
        return test_img_encoding

    def match_face(cls, imgName):
        test_img_encoding = cls.__receive_test_image(imgName)
        matches = face_recognition.compare_faces(cls.known_face_encodings, test_img_encoding)
        id = 0
        face_distances = face_recognition.face_distance(cls.known_face_encodings, test_img_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            id = cls.known_face_names[best_match_index]
        print("マッチした画像のID：" + id)
        return id
