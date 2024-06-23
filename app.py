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

MODELS = ["en_core_web_sm", "en_core_web_md"]

st.title("Learn Natural Language Processing Concepts")

model_selection = st.selectbox("Model name", MODELS)

nlp = spacy.load(model_selection)

input_text = st.text_area("Enter text to be analysed", DEFAULT_TEXT, height = 200)

doc = nlp(input_text)

# visualize_parser(doc, title=None)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title=None, show_table=False)