import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv('car24.csv')

st.dataframe(cars_df.head())

import streamlit as st
import pickle

col1, col2 = st.columns(2)
fuel_type = col1.selectbox('Select Fuel Type', ['Diesel', 'Petrol', 'Hybrid', 'Electric'])
transmission_type = col1.selectbox('Select Transmission', ['Automatic', 'Manual'])
engine = col2.slider('Select Engine Power', 500, 5000, step=100)
seats = col2.selectbox('Select Number of Seats', [4, 5, 7, 9, 11])

encode_dict = {'fuel_type': {'Diesel': 0, 'Petrol': 1, 'Hybrid': 2, 'Electric': 3},
               'transmission_type': {'Automatic': 0, 'Manual': 1}}

def model_pred(fuel_type, transmission, engine_power, seats):
    with open('car_pred', 'rb') as file:
        model = pickle.load(file)
        input_features = [[2018.0, 1, 4000, fuel_type, transmission, 19.70, engine_power, 86.30, seats]]
        return model.predict(input_features)

if st.button('Predict Price'):
    fuel_type_encoded = encode_dict['fuel_type'][fuel_type]
    transmission_encoded = encode_dict['transmission_type'][transmission_type]
    prediction = model_pred(fuel_type_encoded, transmission_encoded, engine, seats)
    st.write(f'Predicted Price: {prediction[0]}')