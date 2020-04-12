import io
import os
import json
import base64
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
# from keras.preprocessing.image import img_to_array
def handle_uploaded_file(f):
    try:
        os.remove('media/temp.jpg')
        with open("media/temp.jpg", 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except Exception as e:
        print("\n++PREDICT.HANDLE_UPLOADED_FILE ",str(e),"++\n")
    
def jsonsolution(label):   
    try:
        if label==403:
                return {"message":"not found"}
        labelfile    =json.load(open('label.json','r'))
        en_Solution_file=json.load(open('En_solution.json','r'))
        gu_Solution_file=json.load(open('Gu_solution.json','r'))
        x=en_Solution_file[labelfile[label]]
        x.update(dict((" "+i,j) for i,j in gu_Solution_file[labelfile[label]].items()))
        return x
        
    except Exception as e:
        print("\n++PREDICT.JSONSOLUTION ",str(e),"++\n")


def handle_RestApi_File(image_data):
    try:
        os.remove('media/temp.jpg')
        x="{}".join(image_data ).encode()
        with open("media/temp.jpg", "wb+") as fh:
                fh.write(base64.decodebytes(x))
    except Exception as e:
        print("\n++PREDICT.HANDLE_RESTAPIFILE ",str(e),"++\n")
    
def predict_fun():
    model=tf.keras.models.load_model('mlmodel/Tomato_model.h5')    
    try:
            img = image.load_img('media/temp.jpg', target_size=(256, 256))    
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict(images)
            x=(list(classes[0])).index(1)
            return str(x)
    except Exception as e:
        print("\n++PREDICT.PREDICT_FUN ",str(e),"++\n")
        return 403