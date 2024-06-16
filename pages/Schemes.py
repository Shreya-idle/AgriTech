import streamlit as st
import pandas as pd

st.set_page_config(page_title="AgriTech",layout="wide",page_icon=None)
def boxed_component():
    excel_file_path = r"./features/govt_scheme.xlsx"
    sheet_name = "Sheet1"
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    row_no = 0
    col_no = 0
    col = st.columns(1)[0]
    while row_no < 27:
        cell_value1 = df.iloc[row_no, col_no]
        cell_value2 = df.iloc[row_no, col_no + 1]
        cell_value3 = df.iloc[row_no, col_no + 2]
        cell_value4 = df.iloc[row_no, col_no + 3]

        with col.container():
            st.markdown(
                f"""
                <div style='border: 2px solid #FBB917; border-radius: 8px; padding: 15px;'>
                    <h2 style='color : #FBB917;'>{cell_value1}</h2>
                    <img src="{cell_value3}" alt="image" width="340"/>
                    <div style='height: 30px;'></div>
                    <p style = "font-size:20px">{cell_value2}</p>
                    <p><a href="{cell_value4}" target="_blank" rel="noopener noreferrer">Go To Site</a></p>
                </div>   
                """,
                unsafe_allow_html=True,
            )
            st.markdown("<br></br>",unsafe_allow_html=True)
        row_no += 1
sch_sen = '''The central and state governments of India have implemented a total of 27 welfare schemes aimed at benefiting farmers across the country. 
These initiatives cover a wide spectrum of agricultural and rural development areas, including financial support, crop insurance, irrigation infrastructure, soil health management, agricultural education, market linkages, and more. 
The schemes aim to enhance agricultural productivity, provide financial assistance, promote sustainable practices, and improve market access for farmers. 
Through these targeted interventions, the governments strive to empower farmers, ensure their welfare, and contribute to the overall growth and sustainability of the agricultural sector, thereby supporting food security and rural development.
'''
# Main Streamlit app
def main():
    # st.title("Schemes for Welfare of Farmers")
    st.markdown(
        f"""
        <h1 style='text-align: center; color: #adc645;'>Government Schemes for Welfare of Farmers</h1>
        <p style = 'font-size:20px'>{sch_sen}</p>
        <hr style='border: 1px solid white;'>
        """,unsafe_allow_html=True,)
    boxed_component()

if __name__ == "__main__":
    main()
