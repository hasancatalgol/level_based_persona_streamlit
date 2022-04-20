#Import Libraries
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Read Data and join both tables
users = pd.read_csv('Data/users.csv')
purchases = pd.read_csv('Data/purchases.csv')
df = purchases.merge(users, how = "inner", on = "uid")



label_country = st.selectbox('Country', ('TUR', 'BRA', 'DEU', 'USA', 'FRA','CAN'))
label_device = st.selectbox('Device', ('AND', 'IOS'))
label_gender = st.selectbox('Gender', ('F', 'M'))
label_age = st.slider('How old are you?', 0, 80, 50)





prediction = print(str(label_country) + "_" + str(label_device) + "_" + str(label_gender) + "_"+ str(label_age))
st.button(label="Predict" , on_click = prediction)



