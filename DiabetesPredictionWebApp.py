# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:11:47 2022

@author: High-Tech
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(r"C:\Users\High-Tech\OneDrive\Desktop\Machine Learning\Machine Learning project\trained_mode.sav" , 'rb'))


def DiabitesPrediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
    
def main():
    
    st.title('Diabites prediction web page')
    
    Pregnancies = st.number_input('Number of Pregnancies' )
    Glucose = st.number_input('Glucose Level')
    BloodPressure = st.number_input('Blood Pressure value')
    SkinThickness = st.number_input('Skin Thickness value')
    Insulin = st.number_input('Insulin Level')
    BMI = st.number_input('BMI value')
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    Age = st.number_input('Age of the Person')

     # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = DiabitesPrediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
     
if __name__ == '__main__':
    main()
    