# Sentiment Analysis
## Table of contents
- [Sentiment Analysis](#sentiment-analysis)
- [Step 1](#step-1)
  - [Folder structure:](#folder-structure)
  - [Project Struture path](#project-struture-path)
- [Step 2](#step-2)
  - [Motivation:](#motivation)
  - [Theoretical Foundation:](#theoretical-foundation)
  - [Argumentation of Choices:](#argumentation-of-choices)
  - [Design, Code, and Artifacts:](#design-code-and-artifacts)
- [Step 3](#step-3)
  - [Interesting study objective](#interesting-study-objective)
  - [Expected Solution](#expected-solution)
  - [Impact and beneficiaries](#impact-and-beneficiaries)
  - [Further development/improvements](#further-developmentimprovements)
- [Step 4](#step-4)
  - [Streamlit](#streamlit)

# Step 1
## Folder structure:
📁Data folder: Includes all data scraped and cleaned data we are working with.

📁Models: Includes the result from our models saved as pickles, to use in our frontend visualiaztion and to compare the models.

📁fetch: Our .py script where we scrape data from Trustpilot.

📁Streamlit: Our frontend visualization with logistic regression using streamlit, guide how to run it is inside Streamlit -> readme

## Project Struture path
📑1_bertopic.ipynb

📑2_dacy_sentiment.ipynb

📑3_bayes.ipynb

📑4_Logistic Regression.ipynb

📑5_performance_comparison.ipynb

📑6. CypherQuery

# Step 2
## Motivation:
The motivation behind this  project is to gain insights into the sentiment of customer reviews on Trustpilot regarding the courier services provided by Postnord, FedEx, and UPS. By scraping and analyzing these reviews, we try to identify patterns, sentiment trends, and potential areas for improvement for each courier service. This information can be valuable for the companies involved in enhancing their customer experience and optimizing their operations.

## Theoretical Foundation:

The project builds upon several theoretical foundations within the field of data science and natural language processing (NLP). Key concepts include sentiment analysis, text classification, and topic modeling.
- **Sentiment Analysis**: It involves determining the sentiment expressed in a given piece of text, whether positive, negative, or neutral. This can be achieved through machine learning algorithms that analyze the contextual information present in the text.
- **Text Classification**: The goal is to categorize text documents into predefined categories based on their content. In this project, we classify the reviews into sentiment categories such as positive, negative, or neutral.
- **Topic Modeling**: It aims to identify the underlying topics or themes within a collection of documents. Here, we utilize the BERTopic algorithm to uncover latent topics in the reviews.
- **Bayes' theorem**: Uses conditional probability to describe the probability of a classification being true given all other factors of a sentence.

## Argumentation of Choices:

The following models were chosen for sentiment analysis based on their performance, popularity, and suitability for this project:
- **BERTopic**: BERTopic is a topic modeling technique that leverages BERT embeddings to cluster similar documents together. By applying BERTopic, we can extract meaningful topics from the reviews, allowing for a deeper understanding of customer sentiments.
- **Bayes Classifier**: The Naive Bayes classifier is a widely used algorithm for text classification tasks. It is efficient and has shown good performance in sentiment analysis applications.
- **Dacy Sentiment**: Dacy is a pre-trained sentiment analysis model that uses the Danish language. Since Trustpilot reviews can be in multiple languages, including Danish, Dacy Sentiment allows us to analyze sentiment accurately in such cases.
- **Logistic Regression**: Logistic regression is a classical statistical method that is often used as a baseline model for text classification tasks. It provides a simple yet interpretable approach to sentiment analysis.

## Design, Code, and Artifacts:

The project consists of the following components:
- **Data Scraping**: We utilized web scraping techniques to collect reviews from Trustpilot for Postnord, FedEx, and UPS. The code for data scraping is implemented using a suitable web scraping package, BeautifulSoup, and customized to extract the necessary information.
- **Preprocessing**: The raw text data obtained from the scraping process is preprocessed to remove punctuation and stopwords. To process the data even further, we could've used techniques like stemming and lemmatization.
- **Feature Extraction**: To represent text data numerically, we get embeddings from transformer-based models like BERT. These embeddings capture the semantic relationships between words and encode them into fixed-length vectors.
- **Model Implementation**: The chosen models, BERTopic, Bayes, Dacy Sentiment, and logistic regression, were implemented using appropriate libraries (e.g., scikit-learn, transformers). Bayes and Logistic Regression were trained on labeled data to learn the sentiment patterns and classify reviews into sentiment categories. Dacy was pretrained and we tested it on the labeled data to evaluate its accuracy.
- **Model Evaluation**: To assess the performance of the sentiment analysis models, we employed appropriate evaluation metrics such as accuracy, precision, recall, and F1-score. We used train-test splits to evaluate the accuracy of the predictions on unknown data to ensure reliable performance. To improve the accuracy of the model further, we could employ k-fold cross-validation during training.


# Step 3
The challenge we would like to address is to compare the sentiment of customer evaluations for organizations/businesses using sentiment analysis and topic modeling on customer reviews from Trustpilot and then use logistic regression with our data and try to predict an unknown sentence that the model havn't seen before.

## Interesting study objective
Customer evaluations are a crucial source of information for organizations to understand the experiences of their clients and to pinpoint areas in need of development. Topic modeling may assist to find the main themes or subjects that consumers are discussing, while sentiment analysis can help to automatically categorize reviews as positive, negative, or neutral. Comparing the tone of customer evaluations for various firms may reveal insightful information about customer preferences and assist companies in gauging their performance against that of their rivals. 

## Expected Solution
A Python program that employs NLP methods to do sentiment analysis and topic modeling on customer reviews of companies on Trustpilot is the anticipated solution. The program would also contrast the tone of customer evaluations for the companies and display the findings using a variety of data visualization tools, including Neo4j, word clouds, bar charts, line graphs, heat maps, scatter plots and more.

## Impact and beneficiaries
The solution can offer insightful information on customer attitude and popular themes, which can help businesses better understand their clientele, identify areas for development, and assess their performance against that of their rivals. Business owners, marketers, customer care agents, and data analysts are among the stakeholders that potentially gain from this solution.

## Further development/improvements 
Build a bot for a target platform, like Discord or Reddit, that reacts and replies to negative or positive comments. This would automate getting in touch with customers who could use support to improve their experience or elicit further feedback.

We could’ve tried many different variants using the BERTopic pipeline trying to tweak the settings for the best results.

We could’ve scraped even more data to get an even better trained model to predict wether a review is positive, negative or neutral. At the same time we could’ve used stemming and lemmatization to cut all the words to their root form, and this could’ve helped the performance aswell + trying to use the text with and without stop words to see any differences.

# Step 4
## Streamlit
We've used Streamlit to create a user interface where you can try our models.

The [requirements.txt](requirements.txt) file specifies the version of Altair to use. This is important as the current version of Streamlit doesn't work with Altair v. 5. As an alternative to installing all dependencies from the requirements file, you can run `pip install "altair<5"` to downgrade that dependency.

```shell
cd Streamlit
streamlit run Sentiment.py
```

Click the GIFs below to play them.

On the **Sentiment** page, you can input a new review, and the program will predict the sentiment and categorize it into a topic.

![](2023-05-25%2016-43-49.gif)

On the **Companies** page, you can compare the different companies in our data. It will show bar and pie charts with the distribution of that companies' reviews' sentiments. It will also show the most common topics for that company.

![](2023-05-25%2017-06-15.gif)