# Power output Prediction
power output prediction using sklearn, FastAPI and Streamlit App

## Table of Contents
-[Description](#description)
-[Requirement](#requirement)
-[Getting started](#getting started)
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
