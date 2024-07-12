"""
A streamlit app for teaching NLP

To run:
In terminal of working directory:
python -m streamlit run app.py
this will open a network url where edits can be
seen in real time on save and refresh
ctrl + c to stop a local streamlit instance
"""

from spacy_streamlit import visualize_ner
import streamlit as st
from annotated_text import annotated_text
import utils

DEFAULT_TEXT = """CELLULAR COMMUNICATIONS INC. sold 1,550,000 common shares at $21.75 each yesterday, \
    according to lead underwriter L.F. Rothschild & Co."""

MODELS = ["en_core_web_sm", "en_core_web_md"]

st.title("Learn Natural Language Processing Concepts")

st.set_page_config(page_title="Learn Natural Language Processing Concepts")

st.markdown("""
    This streamlit app is designed to help teach NLP concepts through 
    **experiential learning**. You can edit the text included in the textbox, 
    press enter, and see how different NLP tokenisation algorithms would 
    split that text into tokens. Use the radio buttons to change between models.
            
    Check out the two sentence tokenisers, spacy_sent and nltk_punkt. Add a second
    sentence to the input text. How do the two sentence tokenisaiton algorithms differ?
    What happens when you add a semi colon between the two sentences?
        
    The second tab 'Part of Speech Tagging' produces a dataframe of 
    each token and some of the parts of speech SpaCy tags that token with.
    You can see an example of how POS tagging is used in **Named Entity 
    Recognition** below the dataframe.
""")

model_selection = st.sidebar.selectbox("Choose a model", MODELS, 0)

st.sidebar.markdown(f"Selected SpaCy model: **`{model_selection}`**")

nlp = utils.load_models(model_selection)

input_text = st.text_area("Enter text to be analysed", DEFAULT_TEXT, height = 100)

doc = nlp(input_text)

tab1, tab2, = st.tabs(["Tokenisation", "Part of Speech Tagging"])

with tab1:

    st.subheader("Tokenisation")

    st.markdown("#### SpaCy models")

    spacy_radio = st.radio("Select an tokeniser:", ["spacy_word", "spacy_sent"],
                        captions= ["SpaCy word tokenisation", "SpaCy sentence tokenisation"],
                        horizontal=True,
                        help= "Choose between different SpaCy word or sentence tokenisers.")

    first_annotate = utils.token_annotator(doc, model = spacy_radio)

    annotated_text(first_annotate)

    st.markdown("#### NLTK models")

    nltk_radio = st.radio("Select an tokeniser:", ["nltk_whitespace", "nltk_treebank", "nltk_twitter", "nltk_punkt"],
                        captions= ["NLTK whitespace tokeniser", "NLTK treebank tokeniser", "NLTK twitter tokeniser",
                                   "NLTK Punkt sentence tokeniser"],
                        horizontal=True,
                        help= "Choose between different NLTK word or sentence tokenisers.")

    second_annotate = utils.token_annotator(doc, model = nltk_radio)

    annotated_text(second_annotate)

with tab2:

    st.subheader("Part of Speech Tagging")
    df = utils.pos_table(doc=doc)
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.subheader("Named Entity Recognition")
    visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title=None, show_table=False)
