# Dog Breed Classifier


Welcome to the Dog Breed Classifier project! This Django web application utilizes a custom deep learning model trained with transfer learning to classify dog breeds based on input images.

## Custom Model

The custom model used in this project has been trained using transfer learning. Transfer learning involves taking a pre-trained model (in this case, likely a model trained on a large dataset like ImageNet) and fine-tuning it on a smaller dataset specific to the task at hand (classifying dog breeds).

### Training Details

- **Base Model**: The base model used for transfer learning is [insert pre-trained model name], which has been pre-trained on a large dataset like ImageNet.
- **Training Dataset**: We used a dataset consisting of thousands of dog images, categorized into different breeds.
- **Transfer Learning Technique**: We employed transfer learning by freezing the convolutional layers of the base model and fine-tuning the fully connected layers to adapt the model to our specific classification task.
- **Training Parameters**: The model was trained with a batch size of [insert batch size], learning rate of [insert learning rate], and for [insert number of epochs].
- **Evaluation Metrics**: During training, we monitored performance using metrics such as accuracy, precision, recall, and F1 score.


## Installation



1. Clone the repository:

   ```bash
   git clone  https://github.com/mheamahfoud/dogbreed.git
2. cd dogbreed   
3.   pip install -r requirements.txt
4.   python manage.py runserver
