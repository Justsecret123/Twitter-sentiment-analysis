# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 02:51:07 2021

@author: Ibrah
"""

import tensorflow as tf

def from_h5_to_export(model):
    
    model.save(output_path)

if __name__ == "__main__":
    
    
    #Read the file path from file
    model_path = "C:\\Users\\Ibrah\\OneDrive\\Bureau\\Projects\\Twitter Sentiment Analysis\\Model\\TSA_model_v1.h5"
    output_path = "C:\\Users\\Ibrah\\OneDrive\\Bureau\\Projects\\Twitter Sentiment Analysis\\Model\\TSA_model_v1"
    
    #Load the model
    model = tf.keras.models.load_model(model_path)
    
    #Conversion
    from_h5_to_export(model)