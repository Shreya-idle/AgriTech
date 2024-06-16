import streamlit as st 
from features.schedule import Schedule 

crop_list = [
'Rice',
'Maize',
 'Chickpea',
 'Kidney Beans',
 'Pigeon Peas',
 'Mothbeans',
 'Mung Bean',
 'Black Gram',
 'Lentil',
 'Pomegranate',
 'Banana',
 'Mango',
 'Grapes',
 'Watermelon',
 'Muskmelon',
 'Apple',
 'Orange',
 'Papaya',
 'Coconut',
 'Cotton',
 'Jute',
 'Coffee']
st.set_page_config(page_title="Vegetable Life Cycle", page_icon="🌱", layout="wide")

# Display the introduction text with a styled header
st.markdown("<h1 style='text-align: center; color: #96aa2e;'>Understanding the Vegetable Life Cycle</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid;'>", unsafe_allow_html=True)
st.markdown("""
##### The life cycle of a vegetable can be broken down into four main stages: pre-planting, planting, vegetative growth, and reproductive growth (fruiting or flowering). Each stage has specific requirements for successful vegetable production.
""")

# Display the stages with descriptions using styled headers and cards
st.markdown("<h2 style='color: #96aa2e;'># Pre-Planting:</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 20px;">
This is the preparatory stage that sets the foundation for healthy plant growth. Here's what happens:
<ul>
<li style='font-size: 20px;'> <strong style = "color : #FBB917" >Soil Preparation<br></strong> The soil is tilled, loosened, and amended to improve drainage, aeration, and nutrient content. This might involve adding compost, manure, or other organic matter. A soil test is often recommended to determine specific nutrient deficiencies that need to be addressed.</li>
<li style='font-size: 20px;'> <strong style = "color : #FBB917" >Seed Selection<br></strong> You choose the right vegetable varieties based on your climate, planting season, and desired harvest. Factors like disease resistance, maturity time, and yield are important considerations.</li>
<li style='font-size: 20px;'> <strong style = "color : #FBB917" >Seed Treatment (Optional)<br></strong> Some seeds may be treated with fungicides or insecticides to protect them from diseases and pests during germination.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #96aa2e;'># Planting:</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 20px;">
This stage involves placing the seeds or seedlings in the soil under the right conditions:
<ul><li style='font-size: 20px;><strong style = "color : #FBB917" >Planting Time<br></strong>The timing depends on the specific vegetable and your local climate. Some vegetables prefer cooler temperatures (e.g., lettuce, spinach) and are planted in early spring or fall, while others thrive in warmer weather (e.g., tomatoes, peppers) and are planted in late spring or early summer.</li>
<li style='font-size: 20px;'><strong style = "color : #FBB917" >Planting Depth and Spacing</strong><br>Seeds are planted at the appropriate depth and spacing for each vegetable variety. Planting depth affects germination success, while spacing allows for proper airflow, light penetration, and root development.</li>
<li style='font-size: 20px;'><strong style = "color : #FBB917" >Watering<br></strong> Newly planted seeds or seedlings require consistent moisture to establish roots and promote germination.</li></ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #96aa2e'># Vegetative Growth:</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 20px;">
This is the active growth stage where the plants focus on developing their leaves, stems, and root systems:
<ul><li style='font-size: 20px;'><strong style = "color : #FBB917">Nutrient Requirements<br></strong> The plants require a balanced supply of nutrients (nitrogen, phosphorus, potassium) for healthy growth. Fertilizer application or organic amendments might be necessary depending on your soil test results.</li>
<li style='font-size: 20px;'><strong style = "color : #FBB917" >Watering<br></strong> Watering needs may vary depending on the weather, plant size, and soil type. The goal is to provide consistent moisture without waterlogging the soil.
<li style='font-size: 20px;'><strong style = "color : #FBB917" >Weed Control<br></strong> Regular weeding is crucial to prevent weeds from competing with your vegetables for light, water, and nutrients.</li>
<li style='font-size: 20px;'><strong style = "color : #FBB917" >Pest and Disease Management<br></strong> Monitoring for pests and diseases is important. Implementing preventative measures or organic controls can minimize damage.</li></ul>
</div>""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #96aa2e'># Reproductive Growth (Fruiting or Flowering):</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 20px;">
This is the final stage where the plant produces its desired harvest:
<ul><li style='font-size: 20px;'><strong style = "color : #FBB917">Focus on Fruit or Flower Development <br></strong> The plant's energy shifts towards developing fruits, flowers, or seeds. Depending on the vegetable, nutrient needs might change, with an increased focus on potassium for fruit development in some cases.</li>
<li style='font-size: 20px;'><strong style = "color : #FBB917">Harvesting <br></strong> Once the fruits, flowers, or seeds reach maturity, it's time for harvest! The timing and method of harvesting will vary depending on the specific vegetable.</li></ul>
</div>""", unsafe_allow_html=True)

# Add some spacing at the bottom for better readability
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<hr>" , unsafe_allow_html=True)
st.markdown("<h4 style='color :#96aa2e;' > Select a crop you want a fertilizer schedule :</h4> ", unsafe_allow_html=True)
option = st.selectbox(
    '',
    crop_list)

# st.markdown(f'<p style="font-size: 20px;">Fertilizer Schedule of <strong><u>{option}</u></strong> :</p> ', unsafe_allow_html=True)
sc = Schedule(option)
st.table(sc.scheduler())