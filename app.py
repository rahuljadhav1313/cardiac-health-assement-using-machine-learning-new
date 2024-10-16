# -- coding: utf-8 --
"""
Created on Wed Aug  7 17:42:24 2024

@author: rahul
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open('C:/Users/rahul/OneDrive/Desktop/Multiple Disease Prediction System/saved model/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/rahul/OneDrive/Desktop/Multiple Disease Prediction System/saved model/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/rahul/OneDrive/Desktop/Multiple Disease Prediction System/saved model/parkinsons_model.sav','rb'))


with st.sidebar:
    selected = option_menu('  Disease Prediction System',

                           ['Cardiac Health Assessment System Using Machine Learning',],
                           
                           menu_icon='hospital-fill',
                           icons=['activity', 'balloon-heart-fill', 'person'],
                           default_index=0)
    
    


# Heart Disease Prediction Page
if selected == 'Cardiac Health Assessment System Using Machine Learning':

    # page title
    st.title('Cardiac Health Assessment System Using Machine Learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)  
