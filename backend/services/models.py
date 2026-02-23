from pydantic import BaseModel
from typing import List


class StartupValidation(BaseModel):
    problem_statement: str
    target_audience: str
    market_opportunity: str
    competitors: List[str]
    differentiation: str
    mvp_features: List[str]
    monetization_model: str
    risks: List[str]
    pitch: str