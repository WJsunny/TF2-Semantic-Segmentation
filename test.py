from __future__ import absolute_import, division, print_function
import tensorflow as tf
from utils.utils import load_image, norm_img, img_to_array
import cv2
#from model.backbone import vgg16,vgg16_subclass
from backbone.all_backbone import Backbones
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16


image = load_image('./images/som2.jpg', resize = (224, 224))
image = norm_img(image)
image = img_to_array(image)

#print(image.ndim)
model_f = Backbones.get_encoder(name = 'vgg16')()
#model_f = model_f(input_shape = (224, 224, 3))
# model_f = vgg16.vgg16(input_shape=(224, 224, 3))
# # model_s = vgg16_subclass.vgg16()
model_k = VGG16()

predictions_f = model_f.predict(image)
# # predictions_s = model_s.predict(image)
predictions_k = model_k.predict(image)

label_f = decode_predictions(predictions_f)
# # label_s = decode_predictions(predictions_s)
label_k = decode_predictions(predictions_k)





print('---'*50)
print('Model_use_FuncAPI: ',label_f[0][:3])
# # print('---'*50)
# # print('Model_use_Subclass: ',label_s[0][:3])
print('---'*50)
print('Model_by_keras: ',label_k[0][:3])