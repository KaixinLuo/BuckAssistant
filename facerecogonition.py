import face_recognition as fcr
import cv2
import os
import re
import numpy as np

def read_face():
    has_face = False
    video_capture = cv2.VideoCapture(0)
    while not has_face:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        has_face = len(fcr.face_locations(rgb_small_frame))!=0
    video_capture.release()
    return rgb_small_frame

class FaceRecognizer:
    def __init__(self,dircetory,list_of_files,tags):
        self.imgs = [fcr.load_image_file(dircetory+file_name) for file_name in list_of_files]
        self.encodings = {t : fcr.face_encodings(data)[0] for (t,data) in zip(tags,self.imgs)}

    def __call__(self,face):
        
        locations = fcr.face_locations(face)
        encodings = fcr.face_encodings(face,locations)
        result = ""
        for unknown_face in encodings:
            matches = fcr.face_distance(list(self.encodings.values()),unknown_face)
            min_val = float("inf")
            for (label,score) in zip(self.encodings.keys(),matches):
                if score<min_val:
                    min_val = score
                    result = label
            
        return result if min_val<0.4 else "Boy Next Door"
                
face_recognizer = FaceRecognizer("./Kaixin/",["KaixinLuo.jpg","ChenLiang.jpeg","HechenZhang.jpeg","boxwell.jpg","ZheLuan.jpeg"],["luo.800","liang.1","zhang.77","boxwell.1","luan.44"])





            
