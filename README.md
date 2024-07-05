<p><a target="_blank" href="https://app.eraser.io/workspace/2t1qZMTObvEXunLBE1zX" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

_View this README file in eraser.io_

# Summative-1

View the app [here](https://summative-1.streamlit.app/).

## Introduction

> Note: If the app has been dormant for a period of time, it might require starting back up again. It will take a few minutes for the hosting service, streamlit, to built.

This `streamlit` app is designed to help teach Natural Language Processing (NLP) concepts. The app allows a user to enter a sentence into the free-text text area and explore how this text can be manipulated by two NLP libraries, `SpaCy` and `NLTK`. 

###  Tokenisation

Tokenisation is an unavoidable primary step in any NLP task, however this is handled differently depending on which tokenisation algorithm is used. This section of the app allows the user to explore the word and sentence tokenisers of SpaCy, and four tokeniser algorithms from NLTK - the whitespace, punkt, treebank, and twitter tokenisers. The user can switch between two language models in SpaCy - `en_core_web_sm` and `en_core_web_md`.

### Part of Speech (POS) tagging

POS tagging is an important element of NLP that helps provide context to words and sentences. It is used in subsequent steps of NLP like dependency parsing. This section of the app allows the user to explore the variety of tags each token is given.

### Dependency tree parsing

An important part in contextual understanding of sentences, understanding the parse tree created by natural language processing models can help to understand the relationship between words in a sentence.

## `SpaCy` language models

The app imports SpaCy language models from the packages GitHub and names the URL path to each language model in the `requirements.txt` file. In app, switching between language models is done using the streamlit `selectbox` function.

<!--- Eraser file: https://app.eraser.io/workspace/2t1qZMTObvEXunLBE1zX --->
