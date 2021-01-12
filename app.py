# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:48:19 2021

@author: hp
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model_spam.pkl', 'rb'))

def predict_default(features):


    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return prediction, probability


def main():

    html_temp = """
        <div style = "background-color: red; padding: 15px;">
            <center><h1><i>EMAIL SPAM FILTERING <i></h1></center>
        </div><br>
        <div style = "background-color: red; padding: 15px;">
            <center><h1><i>DEVELOPED BY Srishti Kumari<i></h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Message = st.text_input("Write your email") 
      
    if st.button("Filter"):
        
        features = [Message]
        prediction, probability = predict_default(features)
        # print(prediction)
        # print(probability[:,1][0])
        if prediction[0] == 1:
            # counselling_html = """
            #     <div style = "background-color: #f8d7da; font-weight:bold;padding:10px;border-radius:7px;">
            #         <p style = 'color: #721c24;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
            #     </div>
            # """
            # st.markdown(counselling_html, unsafe_allow_html=True)

            st.success("This is spam with a probability of {}%.".format(round(np.max(probability)*100, 2)))

        else:
            st.success("This is not a spam with a probability of is {}%.".format(round(np.max(probability)*100, 2)))

      



if __name__ == '__main__':
    main()
