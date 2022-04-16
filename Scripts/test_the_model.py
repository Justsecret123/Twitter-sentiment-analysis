# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 04:10:54 2021

@author: Ibrah
"""
import json
import time
import requests


# API endpoint
SERVER_URL = "http://localhost:8501/v1/models/TSA_model:predict"

# THRESHOLD
THRESHOLD = 0.625

def main():
    """Main"""
    
    # Write down your sentence here 
    examples = [["Messi inserted the clutch gene in PSG. 2 last minute winners in 3 days. MY GOAT"],
                ["Feeling lonely tonight, why do I have to go through this ?"]]
    
    # Create the request
    inputs = list(examples)
    predict_request = json.dumps({'instances': inputs})
    
    # Send few requests to warm-up the model.
    for _ in range(3):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
    
    # Initialize the timer
    print("\nSending request...")
    timer = time.time()
    
    # Send a request to the model
    response = requests.post(SERVER_URL, data=predict_request)
    response.raise_for_status()
    
    # Calculate and display the elapsed time
    timer = round(time.time() - timer, 2)
    print(f"\nElapsed time: {timer}s")
        
    # Get the response
    predictions = response.json()['predictions']
    print(f"\n\nExamples: {[example[0] for example in examples]} ")
    print(f"\n\nPredictions: {predictions}")
    
    # Loop through the results and assign a label
    for prediction in predictions: 
        prediction[0] = "Positive" if prediction[0] > THRESHOLD else "Negative"
    
    # Display results
    print(f"\nOutput: {predictions}")


if __name__ == '__main__':
    main()
    