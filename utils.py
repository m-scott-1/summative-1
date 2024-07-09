"""User defined utility functions used in app.py"""

import spacy
import nltk
import streamlit as st
import pandas as pd

from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer

nltk.download("punkt")

@st.cache_data
def load_models(model):
    """
    Load required SpaCy models
    """
    try:
        nlp = spacy.load(model)
    except Exception as e:
        st.error(f"Error in language model specified.\n{e}.")
        st.stop()

    assert isinstance(nlp, spacy.lang.en.English), "Language model is not an English variant"

    return nlp
# end

def spacy_token_annotator(doc, model):
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
            if a_counter == len(colours):
                a_counter = 0

    elif model == "sent":
        for token in doc.sents:
            annotate.append((str(token), "", colours[a_counter]))
            a_counter +=1
            if a_counter == len(colours):
                a_counter = 0

    return annotate
# end

def nltk_token_annotator(text, model):
    """
    Create data structure whilst annotating text to conform to annotated_text input
    """

    colours = ["#8ef", "#faa", "#afa", "#fea", "#faf", "#baf", "#f83", "#0aa"]
    a_counter = 0
    annotate = []

    if model == "whitespace":
        tk = WhitespaceTokenizer()
    if model == "treebank":
        tk = TreebankWordTokenizer()
    if model == "twitter":
        tk = TweetTokenizer()
    if model == "punkt":
        tk = PunktSentenceTokenizer()

    doc = tk.tokenize(text)

    for token in doc:
        annotate.append((str(token), "", colours[a_counter]))
        a_counter +=1
        if a_counter == len(colours):
            a_counter = 0

    return annotate
# end
