from pydantic import BaseModel
from typing import List
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput
from .market_analyzer import MarketOutput


class CompetitorOutput(BaseModel):
    key_competitors: List[str]
    competitive_intensity: str
    barrier_to_entry: str
    competition_score: int  # 0–10 (higher = more competitive)
    confidence: str


class CompetitorAnalyzer:
    def __init__(self):
        self.llm = LLMService()

    def analyze(
        self,
        idea: str,
        problem_data: ProblemOutput,
        market_data: MarketOutput
    ) -> CompetitorOutput:

        prompt = f"""
You are a startup competitive analyst.

Startup Idea:
"{idea}"

Problem:
{problem_data.problem_statement}

Market Context:
{market_data.market_size_estimate}

Analyze:

1. List key competitors (existing companies or alternatives)
2. Competitive intensity (Low / Medium / High)
3. Barrier to entry
4. Competition pressure score (0-10, where 10 = extremely competitive)
5. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "key_competitors": ["...", "..."],
    "competitive_intensity": "...",
    "barrier_to_entry": "...",
    "competition_score": 0,
    "confidence": "..."
}}
"""

        return self.llm.generate_structured(prompt, CompetitorOutput)