#coding=utf-8
import flask
import os
from io import BytesIO
from PIL import Image
import numpy as np
import json
from easydict import EasyDict
import gdal
import cv2
from skimage import io
import base64

app = flask.Flask(__name__)
LOADED_MODEL = 'resnet'

@app.route('/predict/',methods=['POST'])
def predict():
    data = {'success':False}
    if flask.request.method == 'POST':
        image_url = flask.request.files.get('image')
        image_path_url = flask.request.files.get('image_path')
        config = eval(flask.request.files.get('cfg').read())
        print(config)
        cfg = EasyDict(config)
        print(cfg.BATCH_SIZE)

        if image_url:
            data = {'success':True}
            binary_image = image_url.read()
            # print('xxx {}'.format(image_path_url.read()))
            image = BytesIO(binary_image)
            if image:
                # img = Image.open(image)
                # img = Image.open(image_path_url.read())
                # img.save('2.jpg')
                img = io.imread(image)
                img_str = cv2.imencode('.jpg', img)[1].tostring()  # 将图片编码成流数据，放到内存缓存中，然后转化成string格式
                b64_code = base64.b64encode(img_str)

                data['label'] = 'xxxxxx'
                # data['seg'] = b64_code
                return b64_code
                # return flask.jsonify(data)
            else:
                return flask.jsonify(data)
                
                
if __name__ == '__main__':
    # saved_model_path = 'saved_model_path'
    # sess = load_model(saved_model_path)
    app.run(port='5000')
