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
    Load required SpaCy model with streamlit error handling 
    """
    try:
        nlp = spacy.load(model)
    except Exception as e:
        st.error(f"Error in language model specified.\n{e}.")
        st.stop()

    assert isinstance(nlp, spacy.lang.en.English), "Language model is not an English variant"

    return nlp
# end

def tokenise_text(doc, model: str) -> list[str]:
    """
    Given a tokenisation model, take a string as input and output a list of
    strings based on the tokenisation method of that model
    """

    model_selection = ["spacy_word", "spacy_sent", "nltk_whitespace",
                       "nltk_treebank", "nltk_twitter", "nltk_punkt"]

    assert model in model_selection, st.error(f"Incorrect model name. Choose from: {model_selection}")

    if model == "spacy_word":
        token_list = [str(token) for token in doc]
    if model == "spacy_sent":
        token_list = [str(token) for token in doc.sents]
    if model == "nltk_whitespace":
        token_list = [str(token) for token in WhitespaceTokenizer().tokenize(doc.text)]
    if model == "nltk_treebank":
        token_list = [str(token) for token in TreebankWordTokenizer().tokenize(doc.text)]
    if model == "nltk_twitter":
        token_list = [str(token) for token in TweetTokenizer().tokenize(doc.text)]
    if model == "nltk_punkt":
        token_list = [str(token) for token in PunktSentenceTokenizer().tokenize(doc.text)]
    
    return token_list
# end

def token_annotator(doc, model: str) -> list[tuple[str]]:
    """
    Annotate a list of strings with hex colours in a format conforming to
    the accepted input for the annotated_text package
    """
    
    colours = ["#8ef", "#faa", "#afa", "#fea", "#faf", "#baf", "#f83", "#0aa"]
    counter = 0
    annotate = []
    token_list = tokenise_text(doc, model)
    for token in token_list:
        annotate.append((str(token), "", colours[counter]))
        counter +=1
        if counter == len(colours):
            counter = 0

    return annotate
# end

def pos_table(doc) -> pd.DataFrame:
    """
    Create a DataFrame object that takes each token in a 
    SpaCy doc object and tags them with different parts of speech
    """

    df = pd.DataFrame({
        "Text": [token.text for token in doc],
        "Lemma": [token.lemma_ for token in doc],
        "POS": [token.pos_ for token in doc],
        "POS explained": [spacy.explain(token.pos_) for token in doc],
        "Dependency": [token.dep_ for token in doc]
    })

    return df
# end
