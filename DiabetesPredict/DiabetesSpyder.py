import numpy as np
import pickle

loaded_model = pickle.load(open('C:\\Users\\dharm\\MLProject\\DiabetesPredict\\trained_model.sav','rb'))

input_data =(10,168,74,0,0,38,0.537,34)

#Changing the input data into np array
input_data_asnparray = np.asarray(input_data)

#Reshape the array
input_data_reshape = input_data_asnparray.reshape(1,-1)

#standarized the input data

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if prediction[0]==0:
    print("Patient is non-diabetics")
else:
    print("Patient is diabetic")