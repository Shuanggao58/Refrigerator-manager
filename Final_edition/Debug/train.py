from skimage import io,transform
import glob
import os
import tensorflow as tf
from tensorflow.python.framework import graph_util
#tf.compat.v1.disable_eager_execution()
import numpy as np


os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto(allow_soft_placement=True)
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.33)
config.gpu_options.allow_growth = True


path = "./test_new/"
#model save
model_path = "./module/model"
#Record save address (used to draw neural network structure)  
log_path = "./log"

#input size
w = 100
h = 100
c = 3



def read_image(path):

    global w
    global h
    global c
    cate = [path + x for x in os.listdir(path) if os.path.isdir(path+x)]
    images = []
    labels = []
    for index, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.jpg'):
            img = io.imread(im)
            img = transform.resize(img, (w, h, c))
            images.append(img)
            labels.append(index)
            
    a = np.asarray(images, np.float32)
    b = np.asarray(labels, np.int32)
    return a, b


data, label = read_image(path)
#Shuffle the data set
num_example = data.shape[0]
array = np.arange(num_example)
np.random.shuffle(array)
data = data[array]
label = label[array]
# train:test = 7:3
sample = np.int(num_example * 0.7)
x_train = data[: sample]
y_train = label[: sample]
x_val = data[sample:]
y_val = label[sample:]


# record the change of the neural network
def variable_summaries(var):

    with tf.name_scope('summaries'):
        
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)


# create LeNet-5 NN
def inference(input_tensor, train, regularizer):

    # convolutional layer,input 100 * 100 * 3, output 100 * 100 * 64
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable("weight", [5, 5, 3, 64],initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(conv1_weights)
        conv1_biases = tf.get_variable("bias", [64], initializer=tf.constant_initializer(0.0))
        variable_summaries(conv1_biases)
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))
        tf.summary.histogram('relu1', relu1)

    # pooling layer,input size 100 * 100 * 64, output size 50 * 50 * 64
    with tf.name_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID")
        tf.summary.histogram('pool1', pool1)

    # convolutional layer,input sizew 50 * 50 * 64, output size 50 * 50 * 128
    with tf.variable_scope("layer3-conv2"):
        conv2_weights = tf.get_variable("weight", [5, 5, 64, 128], initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(conv2_weights)
        conv2_biases = tf.get_variable("bias", [128], initializer=tf.constant_initializer(0.0))
        variable_summaries(conv2_biases)
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))
        tf.summary.histogram('relu2', relu2)

    # pooling layer,input size 50 * 50 * 128, output size 25 * 25 * 128
    with tf.name_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
        nodes = 25 * 25 * 128
        reshaped = tf.reshape(pool2, [-1, nodes])
        tf.summary.histogram('pool2', pool2)

    # full connected layer,128 nodes
    with tf.variable_scope('layer5-fc1'):
        fc1_weights = tf.get_variable("weight", [nodes, 128], initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(fc1_weights)
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [128], initializer=tf.constant_initializer(0.1))
        variable_summaries(fc1_biases)
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        # dropout method, the factor is 0.5
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)
        tf.summary.histogram('fc1', fc1)

    # full connected layer,64 nodes
    with tf.variable_scope('layer6-fc2'):
        fc2_weights = tf.get_variable("weight", [128, 64], initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(fc2_weights)
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [64], initializer=tf.constant_initializer(0.1))
        variable_summaries(fc2_biases)
        fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
        # dropout method, the factor is 0.5
        if train:
            fc2 = tf.nn.dropout(fc2, 0.5)
        tf.summary.histogram('fc2', fc2)

    # output layer
    with tf.variable_scope('layer7-fc3'):
        fc3_weights = tf.get_variable("weight", [64, 6], initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(fc3_weights)
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable("bias", [6], initializer=tf.constant_initializer(0.1))
        variable_summaries(fc3_biases)
        logit = tf.matmul(fc2, fc3_weights) + fc3_biases
        tf.summary.histogram('logit', logit)

    return logit



x = tf.placeholder(tf.float32, shape=[None, w, h, c], name='x')
y = tf.placeholder(tf.int32, shape=[None, ], name='y')
# Regularization factor is 0.0001
regularizer = tf.contrib.layers.l2_regularizer(0.0001)
logits = inference(x, True, regularizer)
b = tf.constant(value=1, dtype=tf.float32)
logits_tag = tf.multiply(logits, b, name='softmax')
# loss function
with tf.name_scope('loss'):
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y)
# AdamOptimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cross_entropy)
with tf.name_scope('accuracy'):
    correct_prediction = tf.equal(tf.cast(tf.argmax(logits, 1), tf.int32), y)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar('accuracy', accuracy)



def get_feed_data(inputs=None, targets=None, batch_size=None, shuffle=False):

    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = slice(start_idx, start_idx + batch_size)
        yield inputs[excerpt], targets[excerpt]



epoch = 1
batch_size = 32
saver = tf.train.Saver()
sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter(log_path, sess.graph)
sess.run(tf.global_variables_initializer())
for i in range(epoch):
    #train
    train_loss, train_acc, n_batch = 0, 0, 0
    for x_train_a, y_train_a in get_feed_data(x_train, y_train, batch_size, shuffle=True):
        _, err, ac = sess.run([optimizer, cross_entropy, accuracy], feed_dict={x: x_train_a, y: y_train_a})
        train_loss += err
        train_acc += ac
        n_batch += 1
    print("Epoch: %02d" % (i + 1) + " train loss: %f, train accuracy: %f" % (np.sum(train_loss) / n_batch, np.sum(train_acc) / n_batch))

    # validation
    val_loss, val_acc, n_batch = 0, 0, 0
    for x_val_a, y_val_a in get_feed_data(x_val, y_val, batch_size, shuffle=False):
        summary, err, ac = sess.run([merged, cross_entropy, accuracy], feed_dict={x: x_val_a, y: y_val_a})
        val_loss += err
        val_acc += ac
        writer.add_summary(summary, i)
        n_batch += 1
    print("Epoch: %02d" % (i + 1) + " validation loss: %f, validation accuracy: %f" % (np.sum(val_loss) / n_batch, np.sum(val_acc) / n_batch))

print("training finished.")
saver.save(sess, model_path)

def save_pb(sess):
    constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ['softmax'])
    with tf.gfile.FastGFile("./graph.pb", mode='wb') as f:
        f.write(constant_graph.SerializeToString())   
 
save_pb(sess)

writer.close()
sess.close()
