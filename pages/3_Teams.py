import streamlit as st

st.set_page_config(
    page_title="Players",
    layout="wide"
    )

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clubes", options=clubes)

df_clubes = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_clubes.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)",
           "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_clubes[columns],
             column_config={
                "Overall": st.column_config.ProgressColumn(
                    "Overall", min_value=0, max_value=100, format="%d"),
                "Wage(£)": st.column_config.ProgressColumn(
                    "Weekly Wage", min_value=0, max_value=df_clubes["Wage(£)"].max(), format="£%f"),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
             }
             )