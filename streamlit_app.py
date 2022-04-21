# Web application libraries
import streamlit as st
from streamlit_option_menu import option_menu


# Analytics libraries
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

# Read Data and join both tables
users = pd.read_csv('Data/users.csv')
purchases = pd.read_csv('Data/purchases.csv')
df_ = purchases.merge(users, how="inner", on="uid")
df = df_.copy()

agg_df = df.groupby(["country", "device", "gender", "age"]).agg({"price": "sum"})
agg_df.sort_values("price", ascending=False)
agg_df.reset_index(inplace=True)
agg_df["age_cat"] = pd.cut(agg_df["age"],
                           [0, 18, 25, 35, 50, 65, 80],
                           labels=["0_18", "18_25", "25_35", "35_50", "50_65", "65_80"])

agg_df["customers_level_based"] = [row[0] + "_" + row[1].upper() + "_" + row[2] + "_" + row[5] for row in agg_df.values]
agg_df = agg_df[["customers_level_based", "price"]]

agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("segment").agg({"price": ["count", "min", "max", "mean", "std", "sum"]}).sort_values("segment",
                                                                                                    ascending=False)
agg_df.groupby("segment").agg({"price": "mean"})

# Create a page dropdown

# Header for web application

with st.sidebar:
    selected = option_menu("Main Menu", ['Model', 'Dashboard', 'Contact'],
                           icons=['house', 'clipboard-data', 'person lines fill'], menu_icon="cast",
                           default_index=0)
if selected == 'Model':
    #Header for Model page
    st.header("Level Based Persona - Simple Customer Segmentation")
    # Create drop-down menu items
    countries_st = ["Turkey",
                    "Brazil",
                    "Germany",
                    "United States",
                    "France",
                    "Canada"]

    devices_st = ["Android", "IOS"]
    genders_st = ["Female", "Male"]

    # Sort drop-down menu items because why not?
    countries_st = sorted(countries_st)
    devices_st = sorted(devices_st)
    genders_st = sorted(genders_st)

    # MENU OPTIONS
    label_country = st.selectbox('1)In which country does customer live?', countries_st,
                                 help="Company can't afford to serve other countries at the moment. Stay in touch for further information ")
    label_device = st.radio('2)Which of the following mobile operating systems the customer use?', devices_st)
    label_age = st.number_input('3)How old is the customer?', min_value=0, max_value=80, step=1,
                                help="Oldest clients are only 80 year old!")

    label_gender = st.radio('4)What is gender the customer identifies with?', genders_st,
                            help="Technology soon will be here for our LGTB+ customers :)")

    # Data Preperation for label_country
    if label_country == "Turkey":
        label_country = "TUR"
    elif label_country == "Brazil":
        label_country = "BRA"
    elif label_country == "Germany":
        label_country = "DEU"
    elif label_country == "United States":
        label_country = "USA"
    elif label_country == "France":
        label_country = "FRA"
    elif label_country == "Canada":
        label_country = "CAN"

    # Data Preperation for label_device
    if label_device == "Android":
        label_device = "AND"
    # Data Preperation for genders
    if label_gender == "Female":
        label_gender = "F"
    elif label_gender == "Male":
        label_gender = "M"

    # Data Preperation for age
    if label_age >= 0 and label_age <= 18:
        label_age = "0_18"
    elif label_age > 18 and label_age <= 25:
        label_age = "18_25"
    elif label_age > 25 and label_age <= 35:
        label_age = "25_35"
    elif label_age > 35 and label_age <= 50:
        label_age = "35_50"
    elif label_age > 50 and label_age <= 65:
        label_age = "50_65"
    elif label_age > 65 and label_age <= 80:
        label_age = "65_80"

    new_user = str(label_country + "_" + label_device + "_" + label_gender + "_" + label_age)
    st.spinner(text="In progress...")
    if st.button("Predict"):
        st.dataframe(agg_df[agg_df["customers_level_based"] == new_user])

elif selected == 'Dashboard':
    import streamlit as st
    import plotly.express as px

    st.write("Total sales for each country")
    total_sales = df.groupby(["country"]).agg({"price": "sum"}).sort_values('price', ascending=False)
    total_sales.reset_index(inplace=True)
    fig = px.bar(total_sales, x='country', y='price')
    st.write(fig)

    st.write("Customer Devices")
    device_price = df.groupby(["device"]).agg({"price": "sum"}).sort_values('price', ascending=False)
    device_price.reset_index(inplace=True)
    fig = px.bar(device_price, x='device', y='price')
    st.write(fig)



