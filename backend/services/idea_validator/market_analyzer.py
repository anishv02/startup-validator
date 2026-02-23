from pydantic import BaseModel
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput


class MarketOutput(BaseModel):
    market_size_estimate: str
    growth_potential: str
    trends_supporting_idea: str
    market_score: int
    confidence: str


class MarketAnalyzer:
    def __init__(self):
        self.llm = LLMService()

    def analyze(self, idea: str, problem_data: ProblemOutput) -> MarketOutput:
        prompt = f"""
You are a startup market analyst.

Startup Idea:
"{idea}"

Problem Statement:
{problem_data.problem_statement}

Target Audience:
{problem_data.target_audience}

Analyze:

1. Estimated market size
2. Growth potential
3. Trends supporting idea
4. Market attractiveness score (0-10)
5. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "market_size_estimate": "...",
    "growth_potential": "...",
    "trends_supporting_idea": "...",
    "market_score": 0,
    "confidence": "..."
}}
"""
        return self.llm.generate_structured(prompt, MarketOutput)