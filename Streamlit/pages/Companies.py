import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import streamlit as st

# setting dark theme for matplot because I don't know how to plot the things with Streamlit plots.
#0e1117
#262730
plt.rcParams['figure.facecolor'] = '0e1117'
plt.rcParams['axes.facecolor'] = '0e1117'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

@st.cache_data
def load_data():
    return pd.read_csv('../Data/trustpilot.csv')

st.title("Company comparison")
df = load_data()
companies = df['company'].unique()

selected = st.multiselect("Select companies", companies)
if not selected:
    st.stop()

df_selected = df[df['company'].isin(selected)]
# bar chart
# st.bar_chart(df_selected.groupby('company')['sentiment'].value_counts())
fig, ax = plt.subplots()
ax = sns.countplot(data=df_selected, x='company', hue='sentiment')
for c in ax.containers:
    ax.bar_label(c)
st.pyplot(fig)

# pie charts
fig, (axs,) = plt.subplots(1, len(selected), squeeze=False)
for company, ax in zip(selected, axs):
    ax.pie(df[df['company'] == company].groupby('sentiment').size(), labels=['Negative', 'Neutral', 'Positive'], autopct='%1.1f%%')
    ax.set_title(company)
st.pyplot(fig)

# It would be nice to bring in topics per company.