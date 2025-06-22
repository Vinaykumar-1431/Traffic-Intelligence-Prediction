import streamlit as st
import numpy as np
import pickle
import gzip
import sklearn
with gzip.open("model.pkl.gz","rb") as fp:
    model=pickle.load(fp)
def model_prediction(temp,time,year,date,month,Clear,Clouds,Drizzle,Fog,Haze,Mist,Rain,Smoke,Snow,Squall,Thunderstorm):
    model_value=model.predict(np.array([[temp,time,year,date,month,Clear,Clouds,Drizzle,Fog,Haze,Mist,Rain,Smoke,Snow,Squall,Thunderstorm]]))
    return model_value
    
st.title("Traffic Intelligence System Dashboard Prediction")
col1,col2,col3=st.columns(3)
with col1:
    st.header("Day")
    day=st.number_input("Enter the day",min_value=1,max_value=31,value=1)
with col2:
    st.header("Month")
    month=st.number_input("Enter the month",min_value=1,max_value=12,value=1)
with col3:
    st.header("Year")
    year=st.number_input("Enter the year",min_value=2000,max_value=2050,value=2025)
col4,col5,col6=st.columns(3)
with col4:
    st.header("Time(Hour)")
    hour=st.number_input("Enter the hour",min_value=1,max_value=24,value=1)
with col5:
    st.header("Temperature")
    temp=st.number_input("Enter the temperature in Kelvin",min_value=200,max_value=350,value=280)
with col6:
    st.header("Weather")
    option=st.selectbox("Select the weather condition",["None","Clear","Clouds","Drizzle","Fog","Haze",	"Mist",	"Rain","Smoke","Snow","Squall",	"Thunderstorm"])
Clear=0
Clouds=0
Drizzle=0
Fog=0
Haze=0
Mist=0
Rain=0
Smoke=0
Snow=0
Squall=0
Thunderstorm=0
if(option=="Clouds"):
    Clouds=1
elif(option=="Clear"):
    Clear=1
elif(option=="Drizzle"):
    Drizzle=1
elif(option=="Fog"):
    Fog=1
elif(option=="Haze"):
    Haze=1
elif(option=="Mist"):
    Mist=1
elif(option=="Rain"):
    Rain=1
elif(option=="Smoke"):
    Smoke=1
elif(option=="Snow"):
    Snow=1
elif(option=="Squall"):
    Squall=1
elif(option=="Thunderstorm"):
    Thunderstorm=1
if(st.button("Submit")):
    model_value=model_prediction(temp,hour,year,day,month,Clear,Clouds,Drizzle,Fog,Haze,Mist,Rain,Smoke,Snow,Squall,Thunderstorm)
    st.balloons()
    st.success("The predicted Volume of Traffic is {}".format(model_value))