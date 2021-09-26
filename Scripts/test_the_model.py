# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 04:10:54 2021

@author: Ibrah
"""

import numpy as np
import requests
import json

# Define classes
classes = ["Negative","Positive"]


# API endpoint
SERVER_URL = 'http://localhost:8501/v1/models/TSA_model:predict'
   

def main():
    
    threshold = 0.645
    
    # Write down your sentence here 
    examples = [["Messi inserted the clutch gene in PSG. 2 last minute winners in 3 days. MY GOATTTT"],["United out of the only competition they could dream winning ofLoudly crying faceLoudly crying face"],["Feeling lonely tonight, why do I have to go through this ?"]]
    
    inputs = np.array(examples)
    
    print(f"Inputs shape: {inputs.shape}")

    inputs = list(examples)
    
    
    predict_request = json.dumps({'instances': inputs})
    
    # Send few requests to warm-up the model.
    for _ in range(3):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        
    #Send a request to the model
    response = requests.post(SERVER_URL, data=predict_request)
    response.raise_for_status()
        
    predictions = response.json()['predictions']
    
    
    
    print(f"\n\nPredictions: {predictions}")
    
    input_sentences = [example[0] + "    " for example in examples]
    print(f"\n\nExamples: {input_sentences} ")
    
    
    for prediction in predictions: 
        prediction[0] = "Positive" if prediction[0] > threshold else "Negative"
    
    print(f"\nOutput: {predictions}")
    
    


if __name__ == '__main__':
  main()