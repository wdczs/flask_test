#coding=utf-8
import requests
import json
import numpy as np
import base64
import cv2
from skimage import io


url = 'http://127.0.0.1:5000/predict'
image_path = '5.jpg'
cfg0 = {
    'TRAIN': {'LR': 0.1},
    'BATCH_SIZE': 32
}
cfg_str = str(cfg0)
with open(image_path, 'rb') as f:
    image = f.read() # byte data
payload = {'image': image, 'image_path': image_path, 'cfg': cfg_str}
r = requests.post(url, files=payload)
b64_code = r.content
print()
str_decode = base64.b64decode(b64_code)
nparr = np.frombuffer(str_decode, np.uint8)
img_restore = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
io.imsave('3.jpg', img_restore)
