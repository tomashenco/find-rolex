from sklearn.linear_model import LogisticRegression
import cPickle as pickle
from os import listdir
from os.path import isfile, join
from scipy.ndimage import imread
from scipy.misc import imresize
import numpy as np
import sys


def predict(path, model_file):
    """
    Predicts labels for images and saves result to 'predictions.txt' file
    :param path: path to images
    :param model_file: file with saved model
    """

    # Load model from the file
    print 'Loading model...'
    with open(model_file, 'r') as f:
        lr = pickle.load(f)

    # Load images
    print 'Loading images...'
    files = [f for f in listdir(path) if isfile(join(path, f)) and '.jpg' in f]
    full_files = [join(path, f) for f in files]

    # Load images, resize them to 50x50 colour and flatten
    size = (50, 50, 3)
    images = np.array([imresize(imread(f), size).flatten() for f in full_files])

    # Predict labels for images
    print 'Predicting...'
    y_pred = lr.predict(images)

    # Saving results to the file
    with open('predictions.txt', 'w') as f:
        for file, pred in zip(files, y_pred):
            f.write('%s \t\t %i\n' %(file, pred))

    print 'Finished! You can see the results in predictions.txt'

if __name__ == '__main__':
    predict(sys.argv[1], sys.argv[2])