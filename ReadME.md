# Power output Prediction
power output prediction using sklearn, FastAPI and Streamlit App

## Table of Contents
- [Description](#description)
- [Requirement](#requirement)
- [Getting started](#getting started)
  - [1. Train and save the model](#1-train-and-save-the-model)
  - [2. Deploy FastAPI](#2-deploy-fastapi)
  - [3. Run Streamlit](#3-streamlit)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example input and output](#example-inputand-output)
- [File Structure](#file-structure)
- [License](#license)

## Description
This project provide an API and a streamlit application for predicting power output (PE) based on environmental factors. The model uses Linear Regression from scikit-Learn, trained on features including: 

 - Ambient Temperature (AT)
 - Exhaust Vacuum(V)
 - Ambient Pressure (AP)
 - Relative Humidity (RH)

The API is deployed using FastAPI, and a stream app provides an interactive interface for users to input values and get predictions.

# Requirements
To set up and run this project, you'll need the following python packages:

- 'fastapi'
- 'uvicorn'
- 'scikit-learn'
- 'pandas'
- 'joblib'
- 'numpy'
- 'streamlit'

You can install these dependencies by running:
'''bash
pip install -r requirements,txt
'''

## Getting started
Follow these steps to set up and run the project.

1. Train and save model

   Train a Linear Regression project using Scikit-learn, and save the train model to a file for deployment
   '''bash
   python linear_regression_model.py
   '''

2. Deploy FastAPI
    The FastAPI application ('api.py') loads the saved model and provides an endpoint for predictions. Run it using 'uvicorn'.
   '''bash
   uvicorn api:app --reload 
   '''
 This will start the FastAPI server at 'http://127.0.0.1:8000'

3. Run streamlit 
   The streamlit app allows users to input values and retrieve predictions from the FastAPI server. To 
   '''bash
    streamlit run app.py
   '''

## Usage

FastAPI Endpoints
- POST /predict
  - Description: Accept environmental parameters and returns a predicted power output (PE).
  - Input JSON:
  '''bash
  {
      "ambient_temperature": 45,
      "exhaust_vacuum": 23,
      "ambient_pressure": 45,
      "relative_humidity": 90
  }
  '''
  - Output JSON:
  '''bash
  {
    "prediction": 465.83
  }
  '''

### streamlit Application

 The streamlit app provides an interface for user to input values for 

## Example Input and Output

AT = 15, V = 40, AP = 1000, RH = 75

Example Output:
predicted Power Output (PE) = 465.83


## File structure
The project directory is structured as follows:

'''
📦 linear_regression_app
├─ data
│  └─ data.xlsx
├─ model
│  └─ model.pkl
├─ src
├─ .gitignore
├─ app.py
├─ api.py
├─ linear_regression_model.py
├─ README.md
└─ requirements.txt
'''
## Power Output Visualization

### Actual vs Predicted Values
![Training and Validation Loss](src/linear_regression%20img.png))

## License
This project is licensed under [![License: MIT](...)](...)

