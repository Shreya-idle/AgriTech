import streamlit as st
import requests
from datetime import datetime, timedelta
# Set page configuration
st.set_page_config(
    page_title="Welcome to AgriTech! 👋",
    page_icon="👋",
    layout="wide"
)

# Custom CSS for styling
custom_css = """
<style>

h1, h2, h3, h4, h5 {
    text-align: center;
    color: #96aa2e;
}

hr {
    border: 2px solid #96aa2e;
    
}

main {
    font-size: 20px;
    font-family: Arial, sans-serif;
}

a {
    color: #007BFF;
    text-decoration: none;
}

</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Header
st.markdown("<h1>Welcome to AgriTech! 👋</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div style="font-size: 20px;">
Welcome to AgriTech, your go-to tool for modern farming success! Explore data-driven crop suggestions, mixed cropping optimization, and government schemes information.

<strong style = "font-size:25px ; color: #FBB917 " ><u>Data-Driven Crop Suggestions:</u></strong>
<ul>
<li style = "font-size:20px " >Leverage data analysis for crop suggestions based on soil parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall levels.</li>
<li style = "font-size:20px" >Provide insights into the consequences of growing each suggested crop, aiding informed land use decisions.</li>

<strong style = "font-size:25px ; color: #FBB917"><u>Mixed Cropping Optimization:</u></strong>
<li style = "font-size:20px" >Explore mixed cropping options to enhance soil health and manage pests effectively.</li>

<strong style = "font-size:25px ; color: #FBB917"><u>Government Schemes Information:</u></strong>
<li style = "font-size:20px" >Stay updated on available subsidies and grants through our app, ensuring enhanced agricultural productivity.</li>
<ul>
</div>
""", unsafe_allow_html=True)

# Resources
st.markdown("<h3>Our Resources:</h3>", unsafe_allow_html=True)
st.markdown("""
<div style = "border: 1px solid yellow;padding: 10px;border-radius: 25px">
<ul>
    <li style = "font-size:20px" ><a href='https://www.kaggle.com/datasets/aksahaha/crop-recommendation'>Dataset</a></li>
    <li style = "font-size:20px" >Crop Rotation Dataset: Generated through Bard</li>
    <li style = "font-size:20px" >Consequences dataset: Generated through Bard</li>
</ul>
<div>
""", unsafe_allow_html=True)


def fetch_weather_data(api_key, location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error("Failed to fetch weather data. Please check your location and try again.")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


st.markdown(
"""
<style>
.sidebar .st-ec .st-el:nth-child(2) .subheader {
    color: #adc645;
}
.sidebar-hr {
    border: none;
    border-top: 1px solid #96aa2e;
    margin: 0;
    padding: 0px;
}
.weather-details {
    color: #FBB917;
}
.blink {
    animation: blink 1s infinite;
    color: red; /* Set the text color to red */
}
@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}
</style>
""", unsafe_allow_html=True
)

with st.container():
    st.sidebar.write("---")
    st.markdown(
        """
        <style>
        
        </style>
        """, unsafe_allow_html=True
    )
    st.sidebar.title("Weather Forecast")

    api_key = "3cd8389b57080a9188640f275a4c0774"  
    location = st.sidebar.text_input("Enter City Name", "Varanasi,IN")

    if st.sidebar.button("Get Forecast"):
        weather_data = fetch_weather_data(api_key, location)
        if weather_data:
            try:
                
                current_time = datetime.now()

                
                for i in range(2):
                    forecast = weather_data['list'][i*8]  # Forecast for every 8th data point (3-hour intervals)
                    date = current_time + timedelta(days=i)
                    temperature = forecast['main']['temp']
                    rainfall = forecast.get('rain', {}).get('3h', 0)
                    climate = forecast['weather'][0]['description']
                    humidity = forecast['main']['humidity']

                    st.sidebar.subheader(f"Weather Forecast for {date.strftime('%Y-%m-%d')}")

                    st.sidebar.write(f'<span class="weather-details">**Temperature:** {temperature} °C</span>', unsafe_allow_html=True)
                    st.sidebar.write(f'<span class="weather-details">**Rainfall (last 3 hours):** {rainfall} mm</span>', unsafe_allow_html=True)
                    st.sidebar.write(f'<span class="weather-details">**Climate:** {climate}</span>', unsafe_allow_html=True)
                    st.sidebar.write(f'<span class="weather-details">**Humidity:** {humidity}%</span>', unsafe_allow_html=True)

                    # Blinking effect
                    if i == 0:
                        st.sidebar.markdown(
                            """
                            <style>
                            @keyframes blink {
                                0% { opacity: 1; }
                                50% { opacity: 0; }
                                100% { opacity: 1; }
                            }
                            .sidebar .st-ec .st-el:nth-child(1) .title{
                                color: red;
                            }
                            .blink {
                                animation: blink 1s infinite;
                                color: red; /* Set the text color to red */
                            }
                            </style>
                            """
                        , unsafe_allow_html=True)
                        st.sidebar.markdown('<p class="blink weather-mark">Today\'s Forecast</p>', unsafe_allow_html=True)

                    st.sidebar.write("---")  # Add a separator between days
            except KeyError:
                st.error("Forecast data not available for the specified location. Please try again.")
