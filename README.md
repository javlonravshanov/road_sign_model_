# Introduction
The purpose of this project is to create a robust and accurate model capable of identifying road signs in images. This can be useful for applications such as autonomous driving, traffic monitoring, and road safety systems. The model is built using the fastai library, which provides high-level components for training state-of-the-art machine learning models.

# Dataset
The dataset used for training and testing the model is a combination of the GTSRB - German Traffic Sign Recognition Benchmark dataset and additional road sign images collected manually. The images are organized into different folders, each representing a different class of road sign.

# Dataset Preparation
The dataset was structured and renamed based on categories using the "Bulk Rename Utility" app. This ensured that the images were properly categorized for training the model.

# Directory Structure
The dataset directory structure is as follows:
```
dataset/
├── train/
│   ├── class1/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   ├── class2/
│   └── ...
├── valid/
│   ├── class1/
│   ├── class2/
│   └── ...
```

# Evaluation
The model's performance is evaluated using accuracy on the validation set. The evaluation results are saved and can be reviewed to assess the model's effectiveness.

# Results
After training, the model achieves an accuracy of 99.9% on the validation set when tested with random road sign images.
