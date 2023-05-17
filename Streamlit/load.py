import pickle

import pandas as pd
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

import streamlit as st


@st.cache_resource
def model():
    with open('../Models/bayes.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_resource
def vectorizer():
    with open('../Models/count_vec.pkl', 'rb') as f:
        return pickle.load(f)

# Loading the embedder might not be necessary
@st.cache_resource
def embedder() -> SentenceTransformer:
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

@st.cache_resource
def bertopic() -> BERTopic:
    with open('../Models/bertopic.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_data
def data():
    return pd.read_csv('../Data/trustpilot.csv')