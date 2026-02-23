from .problem_analyzer import ProblemAnalyzer
from .market_analyzer import MarketAnalyzer
from .competitor_analyzer import CompetitorAnalyzer
from .differentiation import DifferentiationStrategist
from .mvp_builder import MVPBuilder
from .monetization import MonetizationPlanner
from .risk_analyzer import RiskAnalyzer


class ValidatorEngine:
    def __init__(self):
        self.problem_analyzer = ProblemAnalyzer()
        self.market_analyzer = MarketAnalyzer()
        self.competitor_analyzer = CompetitorAnalyzer()
        self.differentiation = DifferentiationStrategist()
        self.mvp_builder = MVPBuilder()
        self.monetization = MonetizationPlanner()
        self.risk_analyzer = RiskAnalyzer()

    def evaluate(self, idea: str):

        problem = self.problem_analyzer.analyze(idea)
        market = self.market_analyzer.analyze(idea, problem)
        competition = self.competitor_analyzer.analyze(idea, problem, market)
        differentiation = self.differentiation.analyze(
            idea, problem, market, competition
        )
        mvp = self.mvp_builder.analyze(idea, problem, differentiation)
        monetization = self.monetization.analyze(idea, problem, market)
        risk = self.risk_analyzer.analyze(
            idea, problem, market, competition, mvp
        )

        # Weighted scoring model
        base_score = (
            problem.severity_score * 0.15 +
            market.market_score * 0.2 +
            (10 - competition.competition_score) * 0.15 +
            differentiation.moat_strength_score * 0.15 +
            mvp.execution_feasibility_score * 0.1 +
            monetization.monetization_score * 0.15 +
            differentiation.sustainability_score * 0.1
        )

        final_score = base_score - (risk.risk_penalty_score * 0.15)

        final_score = max(0, min(10, round(final_score, 2)))

        return {
            "problem": problem,
            "market": market,
            "competition": competition,
            "differentiation": differentiation,
            "mvp": mvp,
            "monetization": monetization,
            "risk": risk,
            "final_viability_score": final_score
        }