import os
from glob import glob

dataset_path = '/Users/SmashBros/Documents/GitHub/ReCAPTCHA-Breaker/datasets'

CarData_folder = dataset_path + '/CarData'

train_folder = CarData_folder + '/TrainImages'

negative_folder = train_folder + '/negative/'
positive_folder = train_folder + '/positive/'

print('Dataset Path: \n')
print(os.listdir(dataset_path))

print('CarData Folder: \n')
print(os.listdir(CarData_folder))

print('Positive Folder: \n')
print(os.listdir(positive_folder))

print('Negative Folder: \n')
print(os.listdir(negative_folder))


def load_data():
    return (positive_folder, negative_folder)
