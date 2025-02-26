import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("../datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET")
st.sidebar.markdown("Desenvolvido por [Davi Staaks](https://www.linkedin.com/in/davi-staaks-23b85620a/) no curso da Asimov")

btn = st.button("Acesse os dados do Kaggle")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/")

st.markdown("""
            *** Descrição do meu conjunto de dados ***
                """)