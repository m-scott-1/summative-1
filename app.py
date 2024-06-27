"""
A streamlit app for teaching NLP

To run:
In terminal of working directory:
python -m streamlit run app.py
this will open a network url where edits can be
seen in real time on save and refresh
"""

from spacy_streamlit import visualize_ner
import streamlit as st
import spacy

DEFAULT_TEXT = "Sundar Pichai is the CEO of Google."

MODEL = "en_core_web_sm"

st.title("Learn Natural Language Processing Concepts")

model_selection = st.text(f"Model name {MODEL}")

nlp = spacy.load(MODEL)

input_text = st.text_area("Enter text to be analysed", DEFAULT_TEXT, height = 200)

doc = nlp(input_text)

# visualize_parser(doc, title=None)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title=None, show_table=False)
