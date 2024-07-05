"""
A streamlit app for teaching NLP

To run:
In terminal of working directory:
python -m streamlit run app.py
this will open a network url where edits can be
seen in real time on save and refresh
"""

from spacy_streamlit import visualize_ner, visualize_parser
import streamlit as st
from annotated_text import annotated_text
import pandas as pd
import spacy
import utils

DEFAULT_TEXT = """CELLULAR COMMUNICATIONS INC. sold 1,550,000 common shares at $21.75 each yesterday, \
    according to lead underwriter L.F. Rothschild & Co."""

MODELS = ["en_core_web_sm", "en_core_web_md"]

st.title("Learn Natural Language Processing Concepts")

model_selection = st.sidebar.selectbox("Choose a model", MODELS, 0)

st.sidebar.markdown(f"Selected model: **`{model_selection}`**")

nlp = utils.load_models(model_selection)

input_text = st.text_area("Enter text to be analysed", DEFAULT_TEXT, height = 100)

doc = nlp(input_text)

tab1, tab2, tab3 = st.tabs(["Tokenisation", "Part of Speech Tagging", "Dependency Tree Parsing"])

with tab1:
    st.subheader("Tokenisation")
    st.markdown("#### SpaCy")
    spacy_choice = st.radio("Select a model:", ["word", "sent"], 
                            captions= ["Word tokenisation", "Sentence tokenisation"],
                            horizontal=True)
    spacy_annotate = utils.annotation_wrangler(doc, model = spacy_choice)
    annotated_text(spacy_annotate)
    st.markdown("#### NLTK")

with tab2:
    st.subheader("Part of Speech Tagging")
    df = pd.DataFrame({
        "Text": [token.text for token in doc],
        "Lemma": [token.lemma_ for token in doc],
        "POS": [token.pos_ for token in doc],
        "POS explained": [spacy.explain(token.pos_) for token in doc],
        "Dependency": [token.dep_ for token in doc]
    })
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.subheader("Named Entity Recognition")
    visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title=None, show_table=False)

with tab3:
    st.subheader("Dependency Parsing")
    visualize_parser(doc, title=None)
