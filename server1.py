#coding=utf-8
import flask
import tensorflow as tf
import os

app = flask.Flask(__name__)
#从硬盘中载入模型的结构和权重
def load_model(saved_model_path):
    sess = tf.Session(graph=tf.Graph())
    
    tf.saved_model.loader.load(sess, ['serve'], saved_model_path)
    graph = tf.get_default_graph()
    return sess
    
def model_infer(image_contents):
    global sess
    out = sess.run(['prediction_ori:0','probability_ori:0'], feed_dict={'input_image_as_bytes:0':image_contents})
    return out


@app.route('/predict',methods=['POST'])
def predict():
    data = {'success':False}
    if flask.request.method == 'POST':
        if flask.request.files.get('image'):
            image_path = flask.request.form.get('image_path')
            data = {'success':True}
            image_url = flask.request.files.get('image')
            image = image_url.read()
            if image:
                out = model_infer([image])
                label,prob = out
                
                data['label'] = str(label)
                data['prob'] = str(prob)
                return flask.jsonify(data)
            else:
                return 'There is no image'
                
                
if __name__ == '__main__':
    
    saved_model_path = 'saved_model_path'
    sess = load_model(saved_model_path)
    app.run(host='0.0.0.0',port='8000')
