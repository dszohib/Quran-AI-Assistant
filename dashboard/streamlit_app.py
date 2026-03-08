import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.rag_pipeline import search_quran


st.set_page_config(
    page_title="Quran AI Assistant",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Quran AI Assistant")

st.write(
"""
Ask any question and the AI will return relevant Quran verses.
"""
)

query = st.text_input("Ask your question")

if st.button("Search"):

    answer, verses = search_quran(query)

    st.subheader("AI Answer")
    st.write(answer)

    st.subheader("Relevant Quran Verses")

    for _, row in verses.iterrows():

        st.markdown(f"""
**Surah {row['surah_name']} ({row['surah']}:{row['ayah']})**

Arabic:
{row['arabic']}

Translation:
{row['translation']}
""")