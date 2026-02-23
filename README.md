# 🚀 AI Startup Idea Validator

An AI-powered startup idea validator that analyzes your business idea across multiple dimensions.

## Features

- **Problem Analysis** - Validates the problem statement and target audience
- **Market Analysis** - Estimates market size and growth potential
- **Competition Analysis** - Identifies competitors and barriers to entry
- **Differentiation Strategy** - Suggests unique value propositions
- **MVP Planning** - Recommends core features for MVP
- **Monetization Strategy** - Suggests revenue models
- **Risk Assessment** - Identifies potential risks

## Tech Stack

- **Backend**: FastAPI + LangChain + Groq (LLaMA 3.1)
- **Frontend**: Streamlit

## Local Development

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Research-Copilot
```

### 2. Set up the backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirement.txt
```

### 3. Get your Groq API Key
- Go to [https://console.groq.com/keys](https://console.groq.com/keys)
- Create a free account and generate an API key

### 4. Set environment variable
```bash
export GROQ_API_KEY=your_api_key_here
```

### 5. Run the backend
```bash
uvicorn main:app --reload
```

### 6. Run the frontend (in a new terminal)
```bash
cd frontend
streamlit run startup_validator_app.py
```

## Deployment

### Backend (Render.com)
1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repo and select the `backend` folder
4. Set the environment variable `GROQ_API_KEY`
5. Deploy!

### Frontend (Streamlit Community Cloud)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repo
3. Set the main file path to `frontend/startup_validator_app.py`
4. Add secret `BACKEND_URL` with your Render backend URL
5. Deploy!

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key (get it free at console.groq.com) |
| `BACKEND_URL` | Backend API URL (for frontend deployment) |

## License

MIT
