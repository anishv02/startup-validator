from services.idea_validator.validator_engine import ValidatorEngine

engine = ValidatorEngine()

result = engine.evaluate("AI fitness app for busy developers in India")

print("Final Viability Score:", result["final_viability_score"])