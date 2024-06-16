import streamlit as st
from features import pred 
import pandas as pd 
st.markdown(
    """
    <style>
    .big-font {
        font-family: 'Pacifico', cursive;
        font-size: 36px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
custom_css = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }
    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    .subheader{
        color : #FBB917;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #adc645 ' >🌾Crop Recommendation 🌱 </h1> " , unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #adc645;'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🌱 Soil Parameters:") 
    city = st.text_input(" City Name" ,type="default" )
    
    try:
        city = city.capitalize()
        loc_info = pred.LocationInfo(city)
        humidity , lan , long , temp = loc_info.info()
        temp = float(f"{temp:.2}")
    except:
        temp = 10.0
        humidity = 0
    nitrogen = st.number_input("Nitrogen (kg/ha)", min_value=0.0, max_value=500.0, step=0.1, format="%.1f")
    phosphorus = st.number_input("Phosphorus (kg/ha)", min_value=0.0, max_value=500.0, step=0.1, format="%.1f")
    potassium = st.number_input("Potassium (kg/ha)", min_value=0.0, max_value=500.0, step=0.1, format="%.1f")
    PH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, format="%.1f")

with col2:
    st.subheader("🌦️ Environmental Parameters:")
    temperature = st.number_input("Temperature (°C)", value =temp , min_value=10.0, max_value=50.0, step=0.1, format="%.1f")
    humidity = st.number_input("Humidity (%)", value = humidity ,min_value=0, max_value=100, step=1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, step=1.0)

if st.button("Predict Crop"):
    crop = pred.CropRecommendation(N = nitrogen , Ph = phosphorus,K = potassium,temp = temperature , ph = PH,humidity= humidity,rainfall=rainfall)
    answer = crop.pred()
    styled_answer = f"<span style='font-size:20px ; color:#DAEE01 ;text-decoration: underline;'> {answer.capitalize()}</span>"
    cons = crop.conseqen(answer.lower())
    cons_data = {"Consequences" : cons}
    df = pd.DataFrame(cons_data)
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<hr border: 2px>", unsafe_allow_html=True)
    st.markdown(f"""
                <ul>
                <li style='font-size:20px ; color: #FBB917;'> According to the given parameters, the recommended crop for the field is :{styled_answer}</li>
                <li style = 'font-size:20px ; color : #FBB917'>Consequences to the land after growing the {answer.capitalize()}</li>
                </ul>""", unsafe_allow_html=True)
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    
    
    
    
