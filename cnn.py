#Convolution neural network (CNN)

#Importing keras libraries
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initializing our CNN
classifier = Sequential()

#Step 1-Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation= 'relu'))

#Step 2-Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#Adding another convolution layer to achieve better accuracy
classifier.add(Convolution2D(32, 3, 3, activation= 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#Step 3-Flattening
classifier.add(Flatten())

#Step 4-Full Connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting the CNN to the image
from keras.preprocessing.image import ImageDataGenerator

#Image augmentation
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set', target_size=(64, 64), 
                                                 batch_size=32, class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set', target_size=(64, 64), 
                                            batch_size=32, class_mode='binary')

classifier.fit_generator(training_set, steps_per_epoch=8000, epochs=25, validation_data=test_set, 
                         validation_steps=2000)