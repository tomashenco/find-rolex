import sys
from os import listdir
from os.path import isfile, join
import pandas as pd
from scipy.ndimage import imread
from scipy.misc import imresize
from sklearn.linear_model import LogisticRegression
import cPickle as pickle


def train(path_logo, path_back):
    """
    Trains a logistic regression model for prediction
    Uses technique that was checked in 'research.ipynb'
    :param path_logo: path to the logo images
    :param path_back: path to the background images
    """

    # Find all JPEG files in paths and list them them
    print 'Reading images...'
    back_files = [join(path_back, f) for f in listdir(path_back) if isfile(join(path_back, f)) and '.jpg' in f]
    logo_files = [join(path_logo, f) for f in listdir(path_logo) if isfile(join(path_logo, f)) and '.jpg' in f]

    # Read files, resize them to 50x50 colour and flattened
    size = (50, 50, 3)
    back_images = pd.DataFrame([imresize(imread(f), size).flatten() for f in back_files])
    logo_images = pd.DataFrame([imresize(imread(f), size).flatten() for f in logo_files])

    # Add labels and join logos with background
    back_images['Logo'] = 0
    logo_images['Logo'] = 1
    org_data_set = back_images.append(logo_images)

    # Split to input and output
    X, y = org_data_set.ix[:, :'7499'], org_data_set['Logo']

    # Train logistic regression model
    print 'Training model...'
    lr = LogisticRegression(C=0.001)
    lr.fit(X, y)

    # Export coefficients to file
    coeff = lr.coef_
    with open('model.txt', 'w') as f:
        pickle.dump(lr, f)

    print 'Finished! Model has been saved in: model.txt'

if __name__ == '__main__':
    train(sys.argv[1], sys.argv[2])