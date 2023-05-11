from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

data = pd.read_csv('dacy_sentiment.csv', lineterminator='\n')
sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}
data['sentiment'] = data['sentiment'].replace(sentiment_map)

vectorizer = CountVectorizer(token_pattern=r'\b\w+\b', max_features=1000)
train_vectors = vectorizer.fit_transform(data['body'])
clf = LogisticRegression(random_state=42)
clf.fit(train_vectors, data['sentiment'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_review = request.form['text']
        new_review_vector = vectorizer.transform([new_review])
        predicted_sentiment = clf.predict(new_review_vector)[0]

        if predicted_sentiment == 1:
            sentiment = "Positive sentiment"
        elif predicted_sentiment == 0:
            sentiment = "Neutral sentiment"
        else:
            sentiment = "Negative sentiment"
        return render_template('index.html', sentiment=sentiment)

    return render_template('index.html', sentiment=None)


if __name__ == '__main__':
    app.run(debug=True)
