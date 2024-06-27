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
import utils

DEFAULT_TEXT = """CELLULAR COMMUNICATIONS INC. sold 1,550,000 common shares at $21.75 each yesterday, \
    according to lead underwriter L.F. Rothschild & Co.
"""

MODELS = ["en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"]

st.title("Learn Natural Language Processing Concepts")

model_selection = st.sidebar.selectbox("Choose a model", MODELS, 0)

st.markdown(f"Selected model: **`{model_selection}`**")

nlp = utils.load_models(model_selection)

input_text = st.text_area("Enter text to be analysed", DEFAULT_TEXT, height = 100)

doc = nlp(input_text)

# visualize_parser(doc, title=None)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title=None, show_table=False)
