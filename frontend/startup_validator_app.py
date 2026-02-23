import streamlit as st
import requests
import os

# Use environment variable for deployed backend, fallback to localhost for local dev
API_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="AI Startup Validator", layout="wide")

st.title("🚀 AI Startup Idea Validator")
st.markdown("Enter your startup idea and get a structured evaluation.")

idea = st.text_area("Enter your startup idea:", height=150)

if st.button("Validate Idea"):

    if idea.strip() == "":
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Analyzing idea... This may take 20-40 seconds."):

            response = requests.post(
                f"{API_URL}/validate-idea",
                json={"idea": idea}
            )

            if response.status_code == 200:
                data = response.json()

                st.success(f"Final Viability Score: {data['final_viability_score']} / 10")

                st.subheader("📌 Problem Analysis")
                st.json(data["problem"])

                st.subheader("📈 Market Analysis")
                st.json(data["market"])

                st.subheader("⚔ Competition Analysis")
                st.json(data["competition"])

                st.subheader("🧠 Differentiation Strategy")
                st.json(data["differentiation"])

                st.subheader("🛠 MVP Plan")
                st.json(data["mvp"])

                st.subheader("💰 Monetization")
                st.json(data["monetization"])

                st.subheader("⚠ Risk Assessment")
                st.json(data["risk"])

            else:
                st.error("Error connecting to backend.")