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
    
    # Write down your sentence here 
    examples = [["I feel very nice today"], ["It is a lot stressful for me"], ["is upset that he can t update his facebook by"]]
    
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
        
    prediction = np.squeeze(response.json()['predictions'])
    
    print("Predictions: ", prediction)
    
    output = (prediction)
        
    print(f"\n\nOutput: {output} \n\n\n")


if __name__ == '__main__':
  main()