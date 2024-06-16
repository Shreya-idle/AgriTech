import streamlit as st, matplotlib.pyplot as plt, seaborn as sns
import pandas as pd

st.set_page_config(
    page_title="Minimum Selling Price Trends📈",
    page_icon="📈",
    layout="wide"
)
st.markdown("<h1>Minimum Selling Price Trends📈</h1>", unsafe_allow_html=True)
custom_css = """
<style>
h1 {
    text-align: center;
    color: #3CB043;
    font-weight: bold;
}
.main-container {
    padding: 20px;
  
   
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.plot-container {
    padding: 20px;
}
.selectbox{
    font-size: 20px;
    color: #FFAE42;
}
footer {
    text-align: center;
    padding-top: 20px;
    color: azure;
}
</style>
"""
st.markdown("<hr style='border: 2px solid #adc645;'>", unsafe_allow_html=True)

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("""
<div class="main-container">
<p style = 'font-size:20px' >Explore the Minimum Selling Price (MSP) trends for various crops over the last 10 years. Make informed decisions to maximize your farming profits!</p>
</div>
""", unsafe_allow_html=True)
df = pd.read_csv('features/msp.csv')


selected_crop = st.selectbox('Select Crop', df['crop'])

crop_data = df[df['crop'] == selected_crop].drop(columns=['crop']).squeeze()

plt.figure(figsize=(10, 6))
sns.lineplot(data=crop_data, marker='o', linewidth=2.5, markersize=8, palette='viridis')
plt.xlabel('Year', fontsize=14)
plt.ylabel('MSP (₹/Quintal)', fontsize=14)
plt.title(f'MSP Trends of {selected_crop} Over the Last 10 Years', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.tight_layout()


st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
st.pyplot(plt)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<footer>Happy Farming! 🌾</footer>", unsafe_allow_html=True)
