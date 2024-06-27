"""User defined utility functions. Used in app.py and for testing"""

import spacy
import streamlit as st

@st.cache_data
def load_models(model):
    """
    Load required SpaCy models
    """
    try:
        nlp = spacy.load(model)
    except Exception as e:
        st.error(f"Error in language model specified.\n{e}.")

    assert isinstance(nlp, spacy.lang.en.English), "Language model is not an English variant"

    return nlp
# end
