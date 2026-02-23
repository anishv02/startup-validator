import streamlit as st
import requests
import os

# Use Streamlit secrets for deployed app, environment variable, or fallback to localhost
def get_backend_url():
    # Try Streamlit secrets first (for Streamlit Cloud)
    try:
        return st.secrets["BACKEND_URL"]
    except (KeyError, FileNotFoundError):
        pass
    # Try environment variable
    if os.getenv("BACKEND_URL"):
        return os.getenv("BACKEND_URL")
    # Fallback to localhost for local dev
    return "http://127.0.0.1:8000"

API_URL = get_backend_url()

st.set_page_config(page_title="AI Startup Validator", layout="wide")

st.title("🚀 AI Startup Idea Validator")
st.markdown("Enter your startup idea and get a structured evaluation.")

# Debug: Show which backend URL is being used (remove in production)
st.caption(f"🔗 Connected to: {API_URL}")

idea = st.text_area("Enter your startup idea:", height=150)

if st.button("Validate Idea"):

    if idea.strip() == "":
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Analyzing idea... This may take 60-120 seconds on free tier."):
            try:
                response = requests.post(
                    f"{API_URL}/validate-idea",
                    json={"idea": idea},
                    timeout=300  # 5 minute timeout for LLM processing
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
                    st.error(f"Backend error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.Timeout:
                st.error("Request timed out. The server is taking too long to respond. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error(f"Cannot connect to backend at {API_URL}. Please check if the server is running.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")