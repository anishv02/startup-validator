from pydantic import BaseModel
from typing import List
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput
from .market_analyzer import MarketOutput
from .competitor_analyzer import CompetitorOutput
from .mvp_builder import MVPOutput


class RiskOutput(BaseModel):
    key_risks: List[str]
    technical_risk_level: str
    market_risk_level: str
    execution_risk_level: str
    risk_penalty_score: int  # 0–10 (higher = more risky)
    confidence: str


class RiskAnalyzer:
    def __init__(self):
        self.llm = LLMService()

    def analyze(
        self,
        idea: str,
        problem_data: ProblemOutput,
        market_data: MarketOutput,
        competitor_data: CompetitorOutput,
        mvp_data: MVPOutput
    ) -> RiskOutput:

        prompt = f"""
You are a startup risk analyst.

Startup Idea:
"{idea}"

Problem Severity Score:
{problem_data.severity_score}

Market Score:
{market_data.market_score}

Competition Score:
{competitor_data.competition_score}

Execution Feasibility Score:
{mvp_data.execution_feasibility_score}

Analyze:

1. Key risks (technical, market, execution, regulatory)
2. Technical risk level (Low / Medium / High)
3. Market risk level (Low / Medium / High)
4. Execution risk level (Low / Medium / High)
5. Overall risk penalty score (0-10, higher means riskier)
6. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "key_risks": ["...", "..."],
    "technical_risk_level": "...",
    "market_risk_level": "...",
    "execution_risk_level": "...",
    "risk_penalty_score": 0,
    "confidence": "..."
}}
"""

        return self.llm.generate_structured(prompt, RiskOutput)