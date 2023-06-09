import pickle

import load

import streamlit as st

st.title("Trustpilot Sentiment Analysis")

# load models
vectorizer = load.vectorizer()
model = load.model()
embedder = load.embedder()
bertopic = load.bertopic()
bertopic.calculate_probabilities = True

text = st.text_input("Enter your review here:")
# wait for text input
if not text:
    st.stop()

# make prediction
dtm = vectorizer.transform([text])
pred = model.predict(dtm)[0]
probs = model.predict_proba(dtm)[0]

# show results
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

# Topic modeling
st.subheader("Topic Modeling")
with st.spinner("Analyzing..."):
    embeddings = embedder.encode([text])
    topics, probs = bertopic.transform([text], embeddings)
    
st.write(bertopic.get_topic_info(topics[0]))

desc = probs.argsort()[:, ::-1]
top_n = 3
# tabs
# tabs = st.tabs(list(map(str, range(1, top_n + 1))))
# for i, topic in enumerate(desc[0][:top_n]):
#     with tabs[i]:
#         st.write(bertopic.get_topic_info(topic))
#         st.write("{0:.2%}".format(probs[0][topic]))
       
# cols 
cols = st.columns(top_n)
for i, topic in enumerate(desc[0][:top_n]):
    with cols[i]:
        st.write(bertopic.get_topic_info(topic).loc[0, 'Name'])
        st.write("{0:.2%}".format(probs[0][topic]))