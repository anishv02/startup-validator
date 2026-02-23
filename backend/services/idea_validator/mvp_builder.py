from pydantic import BaseModel
from typing import List
from .llm_service import LLMService
from .problem_analyzer import ProblemOutput
from .differentiation import DifferentiationOutput


class MVPOutput(BaseModel):
    core_features: List[str]
    development_complexity: str
    execution_feasibility_score: int  # 0–10
    confidence: str


class MVPBuilder:
    def __init__(self):
        self.llm = LLMService()

    def analyze(
        self,
        idea: str,
        problem_data: ProblemOutput,
        differentiation_data: DifferentiationOutput
    ) -> MVPOutput:

        prompt = f"""
You are a startup product strategist.

Startup Idea:
"{idea}"

Problem:
{problem_data.problem_statement}

Unique Value Proposition:
{differentiation_data.unique_value_proposition}

Define:

1. Core MVP features (keep minimal and realistic)
2. Development complexity (Low / Medium / High)
3. Execution feasibility score (0-10)
4. Confidence level (low / medium / high)

Respond ONLY in valid JSON:
{{
    "core_features": ["...", "..."],
    "development_complexity": "...",
    "execution_feasibility_score": 0,
    "confidence": "..."
}}
"""

        return self.llm.generate_structured(prompt, MVPOutput)