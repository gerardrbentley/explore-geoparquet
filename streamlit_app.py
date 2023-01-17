import streamlit as st
import geopandas
import folium
import pyarrow
from streamlit_folium import st_folium


@st.experimental_singleton
def load_country_data(file_path: str) -> geopandas.GeoDataFrame:
    gdf = geopandas.read_parquet(file_path)
    return gdf

countries = load_country_data("countries.parquet")
cols = countries.columns
data_cols = cols[~cols.isin(["geometry"])]

st.dataframe(countries[data_cols])


default_display_cols = [
    "TYPE",
    "FORMAL_EN",
    "POP_EST",
    "POP_RANK",
    "GDP_MD_EST",
    "POP_YEAR",
    "LASTCENSUS",
    "GDP_YEAR",
    "ECONOMY",
    "INCOME_GRP",
    "CONTINENT",
    "REGION_UN",
    "SUBREGION",
    "REGION_WB",
]


m = folium.Map(location=[0, 0], zoom_start=2)

column_choice = st.selectbox("Column to Display", cols, cols.get_loc("POP_RANK"))
tooltip_columns = st.multiselect("Columns for Tooltip", cols, default_display_cols)

countries.explore(column_choice, cmap="Blues", m=m, tooltip=tooltip_columns)  

st_folium(m)