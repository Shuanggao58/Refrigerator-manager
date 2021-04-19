import os
from skimage import io, transform
import tensorflow as tf
import numpy as np
import time
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
print(tf.__version__)

class Module:
    def __init__(self):
        self.fruit_dict = {0: 'apple', 1: 'banana', 2: 'bell pepper', 3: 'onion', 4: 'Orange', 5: 'tomato'}
        
        self.w = 100
        self.h = 100
        self.c = 3

    # read image
    def read_image(self, path):
        """img = Image.open(path)
        img.resize((self.h, self.w))
        img = np.asarray(img, dtype=np.float32)
        img = img[:, :, :3]"""
        # resize now doesn't fail
        
        img = io.imread(path)
        img = transform.resize(img, (self.w, self.h,self.c))
        #print(img)
        #print(np.asarray(img1))      
        return np.asarray(img)

    # image reg
    def classification(self, path):
        with tf.Session() as sess:
            data = list()
            data1 = self.read_image(path)
            data.append(data1)
            saver = tf.train.import_meta_graph('./module//model.meta')
            saver.restore(sess, tf.train.latest_checkpoint('./module/'))
            graph = tf.get_default_graph()
            x = graph.get_tensor_by_name("x:0")
            feed_dict = {x: data}
            logits = graph.get_tensor_by_name("logits_tag:0")
            classification_result = sess.run(logits, feed_dict)
            # the prediction for matrix
            print(classification_result)
            # prediction for the biggest index in every rows
            print(tf.argmax(classification_result, 1).eval())
            # gain the result for the image reg on fruit
            output = tf.argmax(classification_result, 1).eval()
            result = "result: \n" + self.fruit_dict[output[0]]
        return result


print("current working directory",os.getcwd())
 


        
try:
    while True:
        try:
            time.sleep(0.01)
            module = Module()
            flag = os.path.isfile(r'/home/pi/RefrigeratorManager/capture.jpg')
            if flag == 1:
                
                string = module.classification(r'/home/pi/RefrigeratorManager/capture.jpg')
                os.remove(r'/home/pi/RefrigeratorManager/capture.jpg')
                print(string)

                with open(r'/home/pi/RefrigeratorManager/result.txt',"w") as f:
                        f.write(string)
                
            else:
                print('pass')
                continue
        except:
            continue
        
except KeyboardInterrupt:
    exit
