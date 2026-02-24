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

        # =============================================================
        # SCORING MODEL v2.0 - Improved score distribution
        # =============================================================
        
        # Softer competition adjustment:
        # Instead of aggressive (10 - score), we use (10 - score * 0.6)
        # This prevents high competition from tanking the score too hard
        adjusted_competition = 10 - (competition.competition_score * 0.6)
        
        # Weighted base score calculation
        base_score = (
            problem.severity_score * 0.15 +           # Problem severity (15%)
            market.market_score * 0.2 +               # Market attractiveness (20%)
            adjusted_competition * 0.15 +             # Competition (softer, 15%)
            differentiation.moat_strength_score * 0.15 +  # Moat strength (15%)
            mvp.execution_feasibility_score * 0.1 +   # MVP feasibility (10%)
            monetization.monetization_score * 0.15 +  # Monetization (15%)
            differentiation.sustainability_score * 0.1    # Sustainability (10%)
        )

        # Reduced risk penalty: 0.08 instead of 0.15
        # Prevents risk from dominating the final score
        risk_adjusted_score = base_score - (risk.risk_penalty_score * 0.08)

        # Mid-range expansion correction:
        # LLMs tend to cluster scores in the 6-8 range, causing final scores
        # to cluster around 5-6. This correction expands the mid-range.
        if 4 <= risk_adjusted_score <= 7:
            final_score = risk_adjusted_score + 0.8
        else:
            final_score = risk_adjusted_score

        # Clamp final score between 0 and 10
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