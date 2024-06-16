import streamlit as st
from features import mixed
import google.generativeai as genai

API_KEY = "AIzaSyDR0CxdqyVVEGxACOBxl0Zi8mdZrzESLEM"
# AIzaSyDPXy1el0qM95-N4HOS5XN4J9i613VWpWM
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(
    page_title="AgriTech - Mixed Cropping",
    page_icon="🌾",
    layout="wide"  
)

# Define crop list
crop_list = [
    'Rice', 'Maize', 'Chickpea', 'Kidney Beans', 'Pigeon Peas', 'Moth Beans',
    'Mung Bean', 'Black Gram', 'Lentil', 'Pomegranate', 'Banana', 'Mango',
    'Grapes', 'Watermelon', 'Muskmelon', 'Apple', 'Orange', 'Papaya',
    'Coconut', 'Cotton', 'Jute', 'Coffee'
]


st.markdown("<h1 style='text-align: center; color: #adc645;'>Select a Crop for Mixed Cropping</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='border: 2px solid #adc645;'>", unsafe_allow_html=True)
st.markdown("""
#### The concept of mixed cropping involves growing two or more crops together to optimize land use and improve yield. Choose a crop from the list below to explore mixed cropping possibilities.
""")


option = st.selectbox(
    '',
    crop_list
)
j =1 

if option:
    st.markdown(f"<h5> Mixed Cropping with <u>{option}</u> </h5>", unsafe_allow_html=True)
    mixed_crop_objects = mixed.MixedCroping(option)
    for i in mixed_crop_objects.mixed_crop():
        res = model.generate_content(f"ratio of seedling for mixed cropping of {option} and {i}")
        st.markdown(f"<h3 style='color: #96aa2e;'>{j}.) {i}</h3>", unsafe_allow_html=True) 
        st.markdown(f"<label style = 'font-size: 20px'> {res.text} </label>", unsafe_allow_html=True)
        st.table(mixed_crop_objects.crop_info(i))
        st.markdown("<hr>",unsafe_allow_html=True)
        j +=1
