# find-rolex
Logo prediction software. Console application that learns from given images and then predict labels for unseen one.

# Install
python setup.py install

# Dependencies
scipy 0.17.0+
numpy 1.10.4+
sklearn 2.7.12+

# Training model
python train_rolex.py path_to_logo_images path_to_background_images

# Prediction
python predict_rolex path_to_images file_with_model
