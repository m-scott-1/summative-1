# Testing module

Import libraries and declare variables

```python

# import libraries

>>> import doctest
>>> from utils import tokenise_text, token_annotator, pos_table
>>> import spacy

>>> nlp = spacy.load("en_core_web_sm")
>>> doc = nlp("This is a test. :-)")
>>> models = ["spacy_word", "spacy_sent", "nltk_whitespace", "nltk_treebank", "nltk_twitter", "nltk_punkt"]

```

## Tests tokenisation function:

```python

>>> for model in models:
...     tokenise_text(doc = doc, model = model)
['This', 'is', 'a', 'test', '.', ':-)']
['This is a test. :-)']
['This', 'is', 'a', 'test.', ':-)']
['This', 'is', 'a', 'test.', ':', '-', ')']
['This', 'is', 'a', 'test', '.', ':-)']
['This is a test.', ':-)']

```

## Tests annotator function:

```python
>>> for model in models:
...     token_annotator(doc = doc, model = model)
[('This', '', '#8ef'), ('is', '', '#faa'), ('a', '', '#afa'), ('test', '', '#fea'), ('.', '', '#faf'), (':-)', '', '#baf')]
[('This is a test. :-)', '', '#8ef')]
[('This', '', '#8ef'), ('is', '', '#faa'), ('a', '', '#afa'), ('test.', '', '#fea'), (':-)', '', '#faf')]
[('This', '', '#8ef'), ('is', '', '#faa'), ('a', '', '#afa'), ('test.', '', '#fea'), (':', '', '#faf'), ('-', '', '#baf'), (')', '', '#f83')]
[('This', '', '#8ef'), ('is', '', '#faa'), ('a', '', '#afa'), ('test', '', '#fea'), ('.', '', '#faf'), (':-)', '', '#baf')]
[('This is a test.', '', '#8ef'), (':-)', '', '#faa')]

```

## Testing part of speech table

```python

>>> df = pos_table(doc = doc)
>>> type(df)
<class 'pandas.core.frame.DataFrame'>

>>> assert len(doc) == len(df)


```