import os
import tensorflow as tf
from tensorflow import keras
from keras import layers,optimizers,datasets

(x,y),(x_val,y_val)=datasets.mnist.load_data()
x=2*tf.convert_to_tensor(x,dtype=tf.float32)/255.-1
y=tf.convert_to_tensor(y,dtype=tf.int32)
y=tf.one_hot(y,depth=10)
print(x.shape,y.shape)
train_dataset=tf.data.Dataset.from_tensor_slices((x,y))
train_dataset=train_dataset.batch(512) 

a=tf.constant([True,False])
aa=tf.cast(a,tf.int32)
print(aa)


b=tf.constant([1,0,2,3])
bb=tf.cast(b,tf.bool)
print(bb)