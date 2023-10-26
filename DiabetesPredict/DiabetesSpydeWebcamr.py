import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open('C:\\Users\\dharm\\MLProject\\DiabetesPredict\\trained_model.sav','rb'))

#Creating function for Prediction

def diabetes_prediction(input_data):

    #Changing the input data into np array
    input_data_asnparray = np.asarray(input_data)

    #Reshape the array
    input_data_reshape = input_data_asnparray.reshape(1,-1)

    #standarized the input data

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if prediction[0]==0:
        return "Patient is non-diabetics"
    else:
        return "Patient is diabetic"
    


def main():
    
    
    #Giving a time
    st.title('Diabetes Prediction Web APP')
    
    #Getting data
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('BloodPressure Value')
    SkinThickness=st.text_input('SkinThichness Value')
    Insulin=st.text_input('Insulin Value')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedi Value')
    Age=st.text_input('Age of Person')
    
    diagnosis=''
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__ =='main':
    main()
    