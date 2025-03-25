import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
import numpy as np


model = pickle.load(open("forest_fire_predictor.pkl", 'rb'))  

def main():
    st.title('Forest Fire Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        temperature = st.number_input('Temperature (°C)', min_value=0.0, value=30.0)
    with col2:
        humidity = st.number_input('Relative Humidity (%)', min_value=0.0, value=57.0)
    with col3:
        wind_speed = st.number_input('Wind Speed (km/h)', min_value=0.0, value=18.0)
    with col1:
        rain = st.number_input('Rain (mm)', min_value=0.0, value=0.0)
    with col2:
        ffmc = st.number_input('FFMC', min_value=0.0, value=65.7)
    with col3:
        dmc = st.number_input('DMC', min_value=0.0, value=3.4)
    with col1:
        dc = st.number_input('DC', min_value=0.0, value=7.6)
    with col2:
        isi = st.number_input('ISI', min_value=0.0, value=1.3)
    with col3:
        bui = st.number_input('BUI', min_value=0.0, value=3.4)
    with col1:
        fwi = st.number_input('FWI', min_value=0.0, value=0.5)

    input_data = pd.DataFrame({
        'Temperature': [temperature],
        'RH': [humidity],
        'Ws': [wind_speed],
        'Rain': [rain],
        'FFMC': [ffmc],
        'DMC': [dmc],
        'DC': [dc],
        'ISI': [isi],
        'BUI': [bui],
        'FWI': [fwi]
    })


    if st.button('Predict'):
        prediction = model.predict(np.array(input_data))  
        # st.write(prediction)
        if prediction[0] == 0:
            st.write(f"Low Risk")
        elif prediction[0] == 1:
            st.write('Moderate Risk')
        else:
            st.write('High Risk')

        # st.success(prediction)

if __name__ == '__main__':
    main()
