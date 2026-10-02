import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Persian Datasets Hub",
    page_icon="🗂️",
    layout="wide",
)

st.title("🗂️ Persian Language Datasets & Corpora")
st.write(
    "A searchable catalog of Persian language resources for "
    "psycholinguistics, cognitive linguistics, and NLP research."
)

@st.cache_data
def load_data():
    return pd.read_csv("datasets.csv")

df = load_data()

# --- Search box ---
search = st.text_input("🔍 Search by name, Persian name, or description...")

if search:
    mask = (
        df["name"].str.contains(search, case=False, na=False)
        | df["persian_name"].str.contains(search, case=False, na=False)
        | df["description"].str.contains(search, case=False, na=False)
    )
    filtered = df[mask]
else:
    filtered = df

st.caption(f"Showing {len(filtered)} of {len(df)} resources")

# --- Table ---
st.dataframe(
    filtered[
        [
            "name",
            "persian_name",
            "description",
            "task_type",
            "size",
            "license",
            "access_level",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

# --- Clickable links ---
st.subheader("🔗 Direct links")
for _, row in filtered.iterrows():
    st.markdown(
        f"**[{row['name']}]({row['link']})** — {row['description']}"
    )

st.markdown("---")
st.caption(
    "Data compiled from published Persian psycholinguistic and "
    "cognitive-linguistic resources."
)
