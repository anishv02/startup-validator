from pydantic import BaseModel
from .llm_service import LLMService


class ProblemOutput(BaseModel):
    problem_statement: str
    target_audience: str
    why_it_matters: str
    severity_score: int  # 0–10
    confidence: str


class ProblemAnalyzer:
    def __init__(self):
        self.llm = LLMService()

    def analyze(self, idea: str) -> ProblemOutput:
        prompt = f"""
You are a startup analyst.

Startup Idea:
"{idea}"

Analyze:

1. Clear problem statement
2. Target audience
3. Why this problem matters
4. Severity score of the problem (0-10)
5. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "problem_statement": "...",
    "target_audience": "...",
    "why_it_matters": "...",
    "severity_score": 0,
    "confidence": "..."
}}
""" 
        return self.llm.generate_structured(prompt, ProblemOutput)