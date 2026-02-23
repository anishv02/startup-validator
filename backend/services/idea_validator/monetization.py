from pydantic import BaseModel
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput
from .market_analyzer import MarketOutput


class MonetizationOutput(BaseModel):
    revenue_model: str
    pricing_strategy: str
    scalability_potential: str
    monetization_score: int  # 0–10
    confidence: str


class MonetizationPlanner:
    def __init__(self):
        self.llm = LLMService()

    def analyze(
        self,
        idea: str,
        problem_data: ProblemOutput,
        market_data: MarketOutput
    ) -> MonetizationOutput:

        prompt = f"""
You are a startup monetization expert.

Startup Idea:
"{idea}"

Target Audience:
{problem_data.target_audience}

Market Context:
{market_data.market_size_estimate}

Analyze:

1. Primary revenue model
2. Pricing strategy
3. Scalability potential
4. Monetization clarity score (0-10)
5. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "revenue_model": "...",
    "pricing_strategy": "...",
    "scalability_potential": "...",
    "monetization_score": 0,
    "confidence": "..."
}}
"""

        return self.llm.generate_structured(prompt, MonetizationOutput)