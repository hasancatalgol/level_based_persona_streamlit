#Import Libraries
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Read Data and join both tables
users = pd.read_csv('Data/users.csv')
purchases = pd.read_csv('Data/purchases.csv')
df_ = purchases.merge(users, how = "inner", on = "uid")
df = df_.copy()




#Header for web application
st.header("Level Based Persona - Simple Customer Segmentation")

#Create drop-down menu items
countries_st = ["Turkey", "Brazil", "Germany", "United States", "France", "Canada"]
devices_st = ["Android", "IOS"]
genders_st = ["Female", "Male"]

#Sort drop-down menu items because why not?
countries_st = sorted(countries_st)
devices_st = sorted(devices_st)
genders_st = sorted(genders_st)


#MENU OPTIONS
label_country = st.selectbox('1)In which country does customer live?', countries_st,
                             help="Company can't afford to serve other countries at the moment. Stay in touch for further information ")
label_device = st.radio('2)Which of the following mobile operating systems the customer use?', devices_st)
label_age = st.number_input('3)How old is the customer?', min_value=0, max_value=80, step=1,
                            help="Oldest clients are only 80 year old!")

label_gender = st.radio('4)What is gender the customer identifies with?', genders_st,
                        help="Technology soon will be here for our LGTB+ customers :)")


#Data Preperation for label_country
if label_country == "Turkey":
    label_country = "TUR"
elif label_country == "Brazil":
    label_country = "BRA"
elif label_country == "Germany":
    label_country = "DEU"
elif label_country == "United States":
    label_country = "USA"
elif  label_country == "France":
    label_country = "FRA"
elif label_country == "Canada":
    label_country = "CAN"

#Data Preperation for label_device
if label_device == "Android":
    label_device= "AND"
#Data Preperation for genders
if label_gender == "Female":
    label_gender = "F"
elif label_gender == "Male":
    label_gender = "M"

#Data Preperation for age
if label_age >= 0 and label_age <= 18 :
    label_age = "0_18"
elif label_age > 18 and label_age <= 25 :
    label_age = "18_25"
elif label_age > 25 and label_age <= 35 :
    label_age = "25_35"
elif label_age > 35 and label_age <= 50 :
    label_age = "35_50"
elif label_age > 50 and label_age <= 65 :
    label_age = "50_65"
elif label_age > 65 and label_age <= 80 :
    label_age = "65_80"


#Button
st.button(label="Predict" )
#st.metric("Customer belongs to ", )








