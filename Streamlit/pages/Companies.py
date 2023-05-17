import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import load

import streamlit as st

# setting dark theme for matplot because I don't know how to plot the things with Streamlit plots.
#0e1117
#262730
plt.rcParams['figure.facecolor'] = '0e1117'
plt.rcParams['axes.facecolor'] = '0e1117'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

def seaborn_barplot():
    fig, ax = plt.subplots()
    ax = sns.countplot(data=df_selected, x='company', hue='sentiment')
    for c in ax.containers:
        ax.bar_label(c)
    st.pyplot(fig)

def piechart(ax):
    ax.pie(df[df['company'] == company].groupby('sentiment').size(), labels=['Negative', 'Neutral', 'Positive'], autopct='%1.1f%%')
    ax.set_title(company)


st.title("Company comparison")
bertopic = load.bertopic()
df = load.data()

companies = df['company'].unique()

selected = st.multiselect("Select companies", companies)
if not selected:
    st.stop()

df_selected = df[df['company'].isin(selected)]

cols = st.columns(len(selected))
for company, col in zip(selected, cols):
    with col:
        # bar charts
        st.bar_chart(df_selected[df_selected['company'] == company].groupby('sentiment').size())
        
        # pie charts
        fig, ax = plt.subplots()
        piechart(ax)
        st.pyplot(fig)


# fig, (axs,) = plt.subplots(1, len(selected), squeeze=False)
# for company, ax in zip(selected, axs):
#     piechart(ax)
# st.pyplot(fig)

# It would be nice to bring in topics per company.