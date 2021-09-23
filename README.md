# Twitter-sentiment-analysis

A sentiment analysis model trained using a Kaggle GPU. Sentiment140 Dataset, with 1.6 million tweets.  

> **Deployed on my personal Docker Hub repository: *Click here* [Click here](https://hub.docker.com/repository/docker/ibrahimserouis/my-tensorflow-models)

> **Kaggle Notebook link:  [Kaggle notebook](https://www.kaggle.com/ibrahimserouis99/twitter-sentiment-analysis)

# Dataset (GloVe)

- Train/test split : 90% / 10% 
- Size : 1.6M samples 
- Link : [Dataset](https://www.kaggle.com/ibrahimserouis99/twitter-sentiment-analysis-and-word-embeddings)


# Model

- Model type : Sequential, RNN, Binary classification
- Optimizer : Adam
- Loss function : Binary cross entropy 
- Outputs : 0 or 1. **0 = negative, 1 = positive**
- Threshold (fine-tuned): 0.644 (>0.644 for a prediction to be labeled as "Positive")
- Best validation accuracy : 83.10%
- Version : 3

# Training 

- Training epochs : **initially** 50, but 18 with early stopping and a patience factor = 10
- Training environment : Kaggle GPU


## Architecture

![Model_architecture](Screenshots/Model%20architecture.png)

# Inferences (with Tensorflow Serving REST API)

![Inference example](Screenshots/Inference%20example.PNG)

# Test script 

[Test script](Scripts/test_the_model.py)

> **There's also a useful script to convert .h5 models to TF SavedModel format [here](Scripts/convert_from_h5_to_TFSavedModel.py)

# Libraries

- Deep Learning Framework : Tensorflow 2.0 or higher 
- Data visualization : Pandas, seaborn, matplotlib
- Regular expressions builder : re 
- NLP library : NLTK, with stopwords
- Train/test splitting, classification_report : Scikit-learn
