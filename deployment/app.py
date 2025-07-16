import streamlit as st
import joblib
from preprocessing import apply_feature_engineer, apply_text_cleaning, apply_tokenizer_lemmatizer

# Load trained pipeline
model = joblib.load("sentiment_model.joblib")

# App title
st.title("🧠 Product Brand Sentiment Classifier")
st.write("Enter a tweet below to predict its sentiment.")

# Input field
tweet = st.text_area("✍️ Enter a tweet:")

# Predict button
if st.button("Predict"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        prediction = model.predict([tweet])
        st.success(f"Predicted Sentiment: **{prediction[0]}**")
