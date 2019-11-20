# -*- coding: utf-8 -*-




from PIL import Image

import os, glob, numpy as np

import sys





from keras.models import load_model


import time

import tensorflow as tf


model = load_model('./Face.h5', compile=False)



seed = 5
tf.set_random_seed(seed)
np.random.seed(seed)

for line in sys.stdin:
    if line.rstrip() == '4':

        while True : 
            time.sleep(0.5)
    
            #caltech_dir = 'input.jpg'
            image_w = 224
            image_h = 224
            pixels = image_h * image_w * 3
            X = []
            filenames = []



            #files = glob.glob("/Users/joyeongjae/Desktop/project/project/jo/"+"input.*")
            #for i, f in enumerate(files):
            img = Image.open("/Users/joyeongjae/Desktop/project/project/jo/input.jpg")
            img = img.convert("RGB")
            img = img.resize((image_w, image_h))
            data = np.asarray(img)

            filenames.append("/Users/joyeongjae/Desktop/project/project/jo/input.jpg")
            X.append(data)
            

            
            X = np.array(X)
            X = X.astype(float) / 255






            prediction = model.predict(X)







            for i in prediction:
                if i[0] >= 0.5: 
                    print("0\n", end='', flush=True) #아기 있음
                    
            
                else :
                    print("1\n", end='', flush=True) #아기 없음
            break        

