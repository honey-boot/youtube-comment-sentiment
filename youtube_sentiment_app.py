import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('youtube_comments_sentiment.csv')

# Title and Description
st.title("🎥 YouTube Comment Sentiment Analysis")
st.markdown("""
Analyze sentiments from top YouTube travel videos!  
This app shows the distribution of Positive, Negative, and Neutral comments.
""")

# Sentiment Pie Chart
st.subheader("🧁 Sentiment Distribution")

sentiment_counts = df['Sentiment'].value_counts()
colors = ['lightgreen', 'lightcoral', 'lightgrey']
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')
st.pyplot(fig)

# Filter option
st.subheader("📂 View Comments by Sentiment")
sentiment_choice = st.selectbox("Choose Sentiment Type", ['Positive', 'Negative', 'Neutral'])
filtered_df = df[df['Sentiment'] == sentiment_choice]
st.write(filtered_df[['Video Title', 'Comment Author', 'Comment Text', 'Likes']].reset_index(drop=True))

# Optional: Download filtered results
st.download_button("⬇️ Download Filtered Comments", filtered_df.to_csv(index=False), file_name='filtered_comments.csv')