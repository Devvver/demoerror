import streamlit as st
import pandas as pd
import streamlit_folium
from streamlit_folium import folium_static
from streamlit_extras.dataframe_explorer import dataframe_explorer
import folium
from folium.plugins import MarkerCluster
from folium import plugins
from folium.plugins import Draw
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import csv

st.set_page_config(page_title="Допомога ВПО в пошуку житла", layout="wide")
uploaded_file = st.file_uploader("Завантажте CSV файл з даними", accept_multiple_files=False)
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("Файл: ", uploaded_file.name)
    uploaded_file.seek(0)
    df = pd.read_csv(uploaded_file,sep=',',encoding='utf-8',low_memory=False)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df["description"].fillna("немає даних", inplace=True)
    df["address"].fillna("немає даних", inplace=True)
    dataframe = df.copy()
    filtered_df = dataframe_explorer(dataframe, case=False)
    if filtered_df is not None:
        st.dataframe(filtered_df, use_container_width=True, height=1200)
    else:
        st.write("Немає данних для фільтрації або помилка вводу")