import streamlit as st
from predictor import Predictor

predictor = Predictor()

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Phishing URL Detection")
st.write("Enter a URL to check whether it is phishing or legitimate.")

url = st.text_input(
    "Enter URL",
    placeholder="https://www.google.com",
    key="url_input"
)

if st.button("Predict"):
    if url == "":
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Analyzing..."):
            result = predictor.predict(url)

        if result is None:
            st.error("Feature extraction failed.")
        else:
            confidence = result["confidence"] * 100

            if result["prediction"] == 1:
                st.error("🚨 Phishing Website")
            else:
                st.success("✅ Legitimate Website")

            st.metric("Confidence", f"{confidence:.2f}%")

            if result.get("warning"):
                st.warning(result["warning"])

            with st.expander("Extracted Features"):
                st.json(result["features"])