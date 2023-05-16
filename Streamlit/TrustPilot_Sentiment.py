import pickle

import streamlit as st

@st.cache_resource
def load_model():
    with open('../Models/bayes.pkl', 'rb') as f:
        return pickle.load(f)

@st.cache_resource
def load_vectorizer():
    with open('../Models/count_vec.pkl', 'rb') as f:
        return pickle.load(f)

vectorizer = load_vectorizer()
model = load_model()

st.title("Trustpilot Sentiment Analysis")

text = st.text_input("Enter your review here:")
dtm = vectorizer.transform([text])
pred = model.predict(dtm)[0]
probs = model.predict_proba(dtm)[0]
# if pred == 1:
#     st.write("Positive")
# elif pred == 0:
#     st.write("Neutral")
# elif pred == -1:
#     st.write("Negative")

colors = {
    1: "green",
    "positive": "green",
    0: "white",
    "neutral": "white",
    -1: "red",
    "negative": "red"
}

st.write(f"Predicted sentiment: :{colors[pred]}[**{pred}**]")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label=":green[Positive]", value="{0:.0%}".format(probs[2]))
with col2:
    st.metric(label="Neutral", value="{0:.0%}".format(probs[1]))
with col3:
    st.metric(label=":red[Negative]", value="{0:.0%}".format(probs[0]))
