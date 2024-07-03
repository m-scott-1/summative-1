"""
User defined utility functions. Used in app.py and for testing

Module level testing:

>>> load_model("en_core_web_sm")
spacy.lang.en.English

"""

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

def annotation_wrangler(doc, model):
    """
    Create data structure whilst annotating text to conform to annotated_text input
    """

    colours = ["#8ef", "#faa", "#afa", "#fea", "#faf", "#baf", "#f83", "#0aa"]
    a_counter = 0
    annotate = []
    if model == "word":
        for token in doc:
            annotate.append((str(token), "", colours[a_counter]))
            a_counter +=1
            if a_counter == 7:
                a_counter = 0

    elif model == "sent":
        for token in doc.sents:
            annotate.append((str(token), "", colours[a_counter]))
            a_counter +=1
            if a_counter == 7:
                a_counter = 0
    
    return annotate
# end
