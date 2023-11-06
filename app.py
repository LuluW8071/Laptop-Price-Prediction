import streamlit as st
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
st.title('Laptop Price Prediction')

# Company Brand
company = st.selectbox('Brand',df['Company'].unique())

# Laptop Type
company = st.selectbox('Type',df['TypeName'].unique())

# RAM
company = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64].unique())

# Weight
weight = st.number_input()

# TouchScreen
touchscreen = st.selectbox('TouchScreen',['Yes', 'No'])

# Display
ips = st.selectbox('IPS',['Yes', 'No'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900',
                                               '3840x2160','3200x1800','2880x1800',
                                               '2560x1600','2560x1440','2304x1440'])

# CPU
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

# GPU
gpu = st.selectbox('GPU',df['Gpu brand'].unique())

# OS
os = st.selectbox('OS',df['os'].unique())