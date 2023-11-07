import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('model/pipe_object.pkl', 'rb'))
df = pickle.load(open('model/laptop_data.pkl', 'rb'))
st.title('Laptop Price Prediction')

# Creating two column layout
left_column, right_column = st.columns(2)

# Left Column
with left_column:
    st.subheader("Basic Laptop Info")
    # Company Brand
    company = st.selectbox('Brand', df['Company'].unique())

    # Laptop Type
    type = st.selectbox('Type', df['TypeName'].unique())

    # RAM
    ram = st.selectbox('RAM(in GB)', [4, 6, 8, 12, 16, 24, 32, 64], index=2)

    # Weight
    weight = st.number_input('Weight of the Laptop(in Kg)', min_value=1.0, max_value=2.8, value=1.8, step=0.1)

# Right Column
with right_column:
    st.subheader("Advanced Laptop Info")
    
    # Create a two-column layout
    left_advanced, right_advanced = st.columns(2)
    
    with left_advanced:
        # TouchScreen
        touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])

        # Display
        ips = st.selectbox('IPS', ['Yes', 'No'])

        # Screen Size
        screen_size = st.selectbox('Screen Size (in Inch)', [13.3, 15.6, 17.3])

        # Resolution
        resolution = st.selectbox('Screen Resolution', ['1920 x 1080', '1366 x 768', '1600 x 900',
                                                        '3840 x 2160', '3200 x 1800', '2880 x 1800',
                                                        '2560 x 1600', '2560 x 1440', '2304 x 1440'])
                
        # OS
        os = st.selectbox('OS', df['os'].unique())

    with right_advanced:
        # CPU
        cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

        # GPU
        gpu = st.selectbox('GPU', df['GpuBrand'].unique())

        # HDD
        hdd = st.selectbox('HDD(in GB)', [0, 256, 512, 1024, 2048])

        # SSD
        ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 512, 1024])

if st.button('Predict Price'):
    # Preprocess input features
    touchscreen = int(touchscreen == 'Yes')
    ips = int(ips == 'Yes')
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

    # Create query array and make the prediction
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]).reshape(1, -1)
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    # Display the result
    st.title(f"\nPrice: {round(predicted_price * 0.012, 2)} USD")

# Note
st.write("""
<span style="color:green">Please note the dataset was collected from Amazon in 2017-18.<br>
Furthermore, only 1301 samples were collected, so the price may be inaccurate.</span>
""", unsafe_allow_html=True)


