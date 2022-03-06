# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 02:51:07 2021

@author: Ibrah
"""

import argparse
import tensorflow as tf

def from_h5_to_export():
    """Converts an H5 model to a TFSavedModel"""
    
    # Parse the command line arguments
    args = parser.parse_args()

    # Get the args as a dict(key,value)
    variables = vars(args)
    
    # Load the model
    print("\nLoading the model...")
    model = tf.keras.models.load_model(variables["source"])
    print("\nDone!")
    
    # Convert and save the output
    model.save(variables["dest"])
    
    print("\nDone!")


def create_parser():
    """Creates a parser for the command line runner"""
    
    # Create the parser
    parser = argparse.ArgumentParser(description="Converts an .h5 model to a TFSavedModel")

    # Add arguments

    # Model path
    parser.add_argument("-source", help="Model path")

    # Output path
    parser.add_argument("-dest", help="Output path")

    return parser


if __name__ == "__main__":
    
    # Constants
    MODEL_PATH = "path to your_model"
    OUTPUT_PATH = "path_to_the_output"
    
    # Setup the parser
    parser = create_parser()
    
    # Conversion
    from_h5_to_export()
    