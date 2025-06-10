import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# Fungsi visualisasi distribusi sentimen
def plot_sentiment_distribution(sentiments):
    plt.figure(figsize=(6,4))
    sns.countplot(x=sentiments, order=['Negatif', 'Netral', 'Positif'])
    plt.title("Distribusi Sentimen")
    plt.xlabel("Sentimen")
    plt.ylabel("Jumlah")
    st.pyplot(plt.gcf())
    plt.clf()

# Fungsi visualisasi word cloud
def plot_wordcloud(texts):
    text_combined = " ".join(texts)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_combined)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud dari Teks")
    st.pyplot(plt.gcf())
    plt.clf()