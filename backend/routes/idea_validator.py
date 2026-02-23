from fastapi import APIRouter
from pydantic import BaseModel
from services.idea_validator.validator_engine import ValidatorEngine

router = APIRouter()

engine = ValidatorEngine()


class IdeaRequest(BaseModel):
    idea: str


@router.post("/validate-idea")
async def validate_idea(request: IdeaRequest):

    result = engine.evaluate(request.idea)

    return {
        "final_viability_score": result["final_viability_score"],
        "problem": result["problem"].dict(),
        "market": result["market"].dict(),
        "competition": result["competition"].dict(),
        "differentiation": result["differentiation"].dict(),
        "mvp": result["mvp"].dict(),
        "monetization": result["monetization"].dict(),
        "risk": result["risk"].dict(),
    }