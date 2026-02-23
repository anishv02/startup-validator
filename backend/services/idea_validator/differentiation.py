from pydantic import BaseModel
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput
from .market_analyzer import MarketOutput
from .competitor_analyzer import CompetitorOutput


class DifferentiationOutput(BaseModel):
    unique_value_proposition: str
    defensibility: str
    moat_strength_score: int  # 0–10
    sustainability_score: int  # 0–10
    confidence: str


class DifferentiationStrategist:
    def __init__(self):
        self.llm = LLMService()

    def analyze(
        self,
        idea: str,
        problem_data: ProblemOutput,
        market_data: MarketOutput,
        competitor_data: CompetitorOutput
    ) -> DifferentiationOutput:

        prompt = f"""
You are a startup strategy expert.

Startup Idea:
"{idea}"

Problem:
{problem_data.problem_statement}

Competition Intensity:
{competitor_data.competitive_intensity}

Key Competitors:
{competitor_data.key_competitors}

Analyze:

1. Unique value proposition
2. How this startup can defend itself against competitors
3. Moat strength score (0-10)
4. Sustainability score (0-10)
5. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "unique_value_proposition": "...",
    "defensibility": "...",
    "moat_strength_score": 0,
    "sustainability_score": 0,
    "confidence": "..."
}}
"""

        return self.llm.generate_structured(prompt, DifferentiationOutput)